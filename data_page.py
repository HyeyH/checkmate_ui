import random
from PyQt5.QtWidgets import (
    QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, 
    QMessageBox, QFileDialog, QDialogButtonBox, 
    QRadioButton, QComboBox, QTextEdit
)
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt
import os
import subprocess
import shutil
from yolo_crop import YoloCrop as YC
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class TutorialDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.currentPage = 1
        self.initUI()

    def initUI(self):
        font_id = QFontDatabase.addApplicationFont("Pretendard-SemiBold.ttf")  
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.setFont(QFont(self.font_family))
        self.setWindowTitle("설명서")
        self.layout = QVBoxLayout()
        self.resize(400, 500)
        self.labels = [
            "Open Dir로 라벨링을 원하는 물품 폴더의 good 또는 bad 폴더를 선택하세요.",
            "Change Save Dir로 라벨링을 원하는 물품 폴더의 labels 폴더를 선택해 주세요.",
            "PascalVOC를 눌러 YOLO로 바꾼다... 이거 맞음??"
            "Create Rect Box로 이미지를 지정해 class를 선택한 후 save 버튼 혹은 Ctrl+S를 눌러 사각형을 저장합니다.",
            "데이터 관리 화면으로 돌아와 해당 물품의 labels 폴더에 저장이 되었는지 확인합니다."
        ]
        self.label = QLabel(self.labels[self.currentPage - 1])
        self.layout.addWidget(self.label)

        # 페이지 수를 표시하는 레이아웃 추가
        self.page_layout = QHBoxLayout()
        self.page_layout.setAlignment(Qt.AlignCenter)
        self.layout.addLayout(self.page_layout)

        self.prev_button = QPushButton("이전")
        self.prev_button.clicked.connect(self.prevPage)
        self.page_layout.addWidget(self.prev_button)

        self.page_label = QLabel(f"페이지: {self.currentPage}/{len(self.labels)}")
        self.page_layout.addWidget(self.page_label)

        self.next_button = QPushButton("다음")
        self.next_button.clicked.connect(self.nextPage)
        self.page_layout.addWidget(self.next_button)

        self.setLayout(self.layout)

        # 다이얼로그를 오른쪽에 위치시킵니다.
        screen_geometry = QApplication.desktop().screenGeometry()
        dialog_geometry = self.geometry()
        self.move(screen_geometry.width() - dialog_geometry.width(), int((screen_geometry.height() - dialog_geometry.height()) / 2))

    def nextPage(self):
        self.currentPage += 1
        if self.currentPage <= len(self.labels):
            self.label.setText(self.labels[self.currentPage - 1])
            self.page_label.setText(f"페이지: {self.currentPage}/{len(self.labels)}")
        else:
            self.currentPage = len(self.labels)
    
    def prevPage(self):
        self.currentPage -= 1
        if self.currentPage >= 1:
            self.label.setText(self.labels[self.currentPage - 1])
            self.page_label.setText(f"페이지: {self.currentPage}/{len(self.labels)}")
        else:
            self.currentPage = 1

class DataPage(QDialog):
    def __init__(self):
        super().__init__()
        font_id = QFontDatabase.addApplicationFont("Pretendard-SemiBold.ttf")  
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.setFont(QFont(self.font_family))
        
    def open_ratio_data(self):
        dialog = QDialog()
        dialog.resize(500, 400)
        layout = QVBoxLayout()

        self.directory_combo = QComboBox()
        self.populate_directory_combo()
        layout.addWidget(self.directory_combo)
        
        # 비율을 지정하기 위한 레이블과 입력 필드를 추가합니다.
        self.ratio_label = QLabel("데이터 분할 비율을 선택해 주세요. 순서대로 train:valid:test 입니다.\n비율이 딱 떨어지지 않는 경우 train에 남는 데이터가 추가됩니다.")
        layout.addWidget(self.ratio_label)

        self.radio_602020 = QRadioButton("60:20:20")
        self.radio_603010 = QRadioButton("60:30:10")
        self.radio_702010 = QRadioButton("70:20:10")
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_602020)
        radio_layout.addWidget(self.radio_603010)
        radio_layout.addWidget(self.radio_702010)    
        layout.addLayout(radio_layout)

        # 분할 버튼을 추가합니다.
        self.split_button = QPushButton("데이터 분할")
        self.split_button.clicked.connect(self.split_data)
        layout.addWidget(self.split_button)

        dialog.setLayout(layout) 
        dialog.exec_()

    def populate_directory_combo(self):
        # './data' 디렉터리에서 디렉터리 명들을 읽어와 콤보박스에 추가합니다.
        directory = './data'
        directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
        self.directory_combo.addItems(directories)

    def split_data(self):
        directory_name = self.directory_combo.currentText()
        directory = os.path.join('data', directory_name)

        image_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
        if not image_files:
            QMessageBox.warning(self, "경고", "이미지가 없어 분할을 진행할 수 없습니다.")
            return

        random.shuffle(image_files)  # 이미지 파일들을 랜덤으로 섞음

        label_files = [f[:-4] + '.txt' for f in image_files if f[:-4] + '.txt' in os.listdir(directory)]
        if len(label_files) != len(image_files):
            QMessageBox.warning(self, "경고", "이미지와 레이블 파일의 수가 일치하지 않습니다.")
            return

        if self.radio_603010.isChecked():
            ratio_text = "60:30:10"
        elif self.radio_602020.isChecked():
            ratio_text = "60:20:20"
        elif self.radio_702010.isChecked():
            ratio_text = "70:20:10"  
        else:
            QMessageBox.warning(self, "경고", "원하는 분할 비율을 선택하세요.")
            return

        try:
            # 입력된 비율을 ':'로 분할하여 train, valid, test 비율로 나눕니다.
            ratios = ratio_text.split(':')
            if len(ratios) != 3:
                QMessageBox.warning(self, "Error", "올바른 비율을 입력하세요.")
                return
            
            train_ratio, valid_ratio, test_ratio = map(lambda x: float(x) * 0.01, ratios)

            # 디렉터리 생성
            train_dir = os.path.join(directory, 'train')
            valid_dir = os.path.join(directory, 'valid')
            test_dir = os.path.join(directory, 'test')
            for folder in [train_dir, valid_dir, test_dir]:
                if os.path.exists(folder):
                    shutil.rmtree(folder)
                os.makedirs(os.path.join(folder, 'images'), exist_ok=True)
                os.makedirs(os.path.join(folder, 'labels'), exist_ok=True)

            # 파일을 train, valid, test로 분할하여 복사
            total_files = len(image_files)
            train_count = int(train_ratio * total_files)
            valid_count = int(valid_ratio * total_files)
            test_count = int(test_ratio * total_files)
            train_count += total_files - train_count - valid_count - test_count

            print(f"total{total_files} train{train_count} valid{valid_count} test{test_count}")

            for i in range(total_files):
                image_file = image_files[i]
                label_file = label_files[i]
                dest_folder = None

                if i < train_count:
                    dest_folder = 'train'
                elif i < train_count + valid_count:
                    dest_folder = 'valid'
                else:
                    dest_folder = 'test'

                image_dest = os.path.join(directory, dest_folder, 'images', image_file)
                label_dest = os.path.join(directory, dest_folder, 'labels', label_file)

                shutil.copy(os.path.join(directory, image_file), image_dest)
                shutil.copy(os.path.join(directory, label_file), label_dest)

            QMessageBox.information(self, "완료", "데이터 분할이 완료되었습니다.")
        except Exception as e:
            QMessageBox.warning(self, "에러", str(e))

    def open_label_data(self):
        dialog = QDialog()
        dialog.resize(500, 400)
        layout = QVBoxLayout()
        label = QLabel("데이터를 라벨링할 물품의 이름을 하나만 입력하세요. 예) eraser")
        layout.addWidget(label)
        text_edit = QTextEdit()
        text_edit.setFixedHeight(30)
        layout.addWidget(text_edit)
        button_ok = QPushButton("확인")

        def on_button_ok_clicked():
            item_name = text_edit.toPlainText().strip()  # text_edit의 텍스트를 가져옴 (양쪽 공백 제거)
            if not item_name:
                QMessageBox.warning(self, "경고", "물품명을 입력하세요.")
                return
            else:
                self.image_directory = os.path.join("data", item_name)
                # good 디렉터리가 존재하고 비어 있지 않은지 확인
                if os.path.exists(self.image_directory):
                    jpg_files = [f for f in os.listdir(self.image_directory) if f.endswith('.jpg')]
                    if not jpg_files:  # 디렉터리 내에 jpg 파일이 없는 경우
                        QMessageBox.warning(self, "경고", "디렉터리에 이미지가 있어야 합니다.")
                        return
                else:
                    QMessageBox.warning(self, "경고", "디렉터리가 존재하지 않습니다.")
                    return

                # 이미지가 있는 경우에만 라벨링 가능 메시지 표시
                QMessageBox.information(self, "알림", "이미지 라벨링이 가능합니다.")
                dialog.close()
                exe_path = os.path.join("labelImg", 'labelImg.exe')
                if os.path.exists(exe_path) and exe_path.endswith(".exe"):
                    # labelImg.exe 파일이 존재하고 확장자가 .exe인 경우 실행
                    process = subprocess.Popen([exe_path])
                    process.wait()  # labelImg.exe가 실행되는 동안 대기

                    # labelImg.exe가 종료되면 crop_yolo.py 실행
                    if process.returncode == 0:  # labelImg.exe가 정상 종료되었을 때
                        yolo_crop = YC()
                        yolo_crop.setpath(self.image_directory, os.path.join(self.image_directory, 'good_crop'))
                        listofall = os.listdir(yolo_crop.input_path)
                        listofjpg = [file for file in listofall if file.endswith(".jpg") or file.endswith(".JPG")]
                        listoftag = [file for file in listofall if file.endswith(".txt") or file.endswith(".TXT")]
                        for i in range(len(listofjpg)):
                            yolo_crop.openfile(listoftag[i], listofjpg[i])

                    else:
                        QMessageBox.warning(self, "Error", "labelImg 실행 중 오류가 발생했습니다.")
                else:
                    QMessageBox.warning(self, "Error", "labelImg.exe 파일을 찾을 수 없거나 확장자가 올바르지 않습니다.")
        button_ok.clicked.connect(on_button_ok_clicked)
        layout.addWidget(button_ok)
        dialog.setLayout(layout)
        dialog.exec_()

    def open_add_data(self):
        dialog = QDialog(self)
        dialog.setFont(QFont(self.font_family))
        dialog.setWindowTitle("데이터 추가")
        dialog.resize(500, 400)
        item_label = QLabel("추가할 데이터의 이름을 영문으로 작성해 주세요. 예) eraser, milk")

        self.item_name = QTextEdit()  
        item_layout = QVBoxLayout()
        item_layout.addWidget(item_label)
        item_layout.addWidget(self.item_name)

        # 파일 찾기 버튼 생성
        self.files = None
        file_label = QLabel("추가할 데이터 파일들을 선택해 주세요.")
        self.selected_files_label = QLabel()  # 선택된 파일 이름을 나타낼 라벨
        file_button = QPushButton("파일 찾기")
        file_button.clicked.connect(self.open_file_dialog)
        file_layout = QVBoxLayout()
        file_layout.addWidget(file_label)
        file_layout.addWidget(self.selected_files_label)
        file_layout.addWidget(file_button)
        
        # Dialog layout 생성
        layout = QVBoxLayout()
        layout.addLayout(item_layout)
        layout.addSpacing(20)  # 간격 추가
        layout.addLayout(file_layout)
        layout.addSpacing(40)  # 간격 추가
        
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.add_data)
        button_box.button(QDialogButtonBox.Ok).setText("확인")
        
        layout.addWidget(button_box)
        dialog.setLayout(layout)
        
        dialog.exec_()

    def add_data(self):
        # 사용자가 입력한 데이터 이름 가져오기
        item_name_text = self.item_name.toPlainText().strip()
        
        if not item_name_text:
            QMessageBox.warning(self, "경고", "데이터 이름을 입력하세요.")
            return
        
        # 새 디렉터리 생성
        directory = os.path.join('data', item_name_text)
        os.makedirs(directory, exist_ok=True)
        
        if not self.files:
            QMessageBox.warning(self, "경고", "추가할 데이터를 선택하세요.")
            return
        else:
            for file in self.files:
                src_file = file  # 파일 경로
                dest_file = os.path.join(directory, os.path.basename(file))  # 대상 디렉토리에 파일 복사
                if os.path.exists(dest_file):
                    choice = QMessageBox.question(self, "파일 덮어쓰기", 
                                                f"파일 '{os.path.basename(dest_file)}'가 이미 존재합니다. 덮어쓰시겠습니까?",
                                                QMessageBox.Yes | QMessageBox.No)
                    if choice == QMessageBox.Yes:
                        try:
                            os.remove(dest_file)
                            # 해당 파일의 확장자가 .jpg나 .JPG인 경우 동일한 이름의 txt 파일도 함께 삭제
                            base_name, ext = os.path.splitext(os.path.basename(dest_file))
                            if ext.lower() in ['.jpg', '.jpeg']:
                                txt_file = os.path.join(directory, base_name + '.txt')
                                if os.path.exists(txt_file):
                                    os.remove(txt_file)
                            shutil.copy(src_file, dest_file)
                        except Exception as e:
                            QMessageBox.warning(self, "오류", f"파일을 덮어쓰는 중 오류가 발생했습니다: {e}")
                    else:
                        new_filename, ext = os.path.splitext(os.path.basename(dest_file))
                        i = 1
                        while os.path.exists(os.path.join(directory, f"{new_filename}_{i}{ext}")):
                            i += 1
                        new_file = os.path.join(directory, f"{new_filename}_{i}{ext}")
                        try:
                            shutil.copy(src_file, new_file)
                        except Exception as e:
                            QMessageBox.warning(self, "오류", f"새 파일을 복사하는 중 오류가 발생했습니다: {e}")
                else:
                    try:
                        shutil.copy(src_file, dest_file)
                    except Exception as e:
                        QMessageBox.warning(self, "오류", f"파일을 복사하는 중 오류가 발생했습니다: {e}")
        
        QMessageBox.information(self, "완료", "데이터 추가가 완료되었습니다.")

    def open_file_dialog(self):
        options = QFileDialog.Options()
        self.files, _ = QFileDialog.getOpenFileNames(self, "파일 선택", "", "All Files (*);;", options=options)
        if self.files:
            self.selected_files_label.setWordWrap(True)
            self.selected_files_label.setText("선택된 파일: " + ", ".join(self.files))
