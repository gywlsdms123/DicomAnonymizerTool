import time
import sys
import os
from tqdm import tqdm
import pydicom
from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QIcon
from gui import main


class AnonymizeApp(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super(AnonymizeApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Dicom Anonymized Tool")
        self.setWindowIcon(QIcon('dicom.ico'))
        self.btnStart.clicked.connect(self.start_thread)
        self.btnStop.clicked.connect(self.btnStop_clicked)
        self.btnPath.clicked.connect(self.btnPath_clicked)

    # 파일 경로 불러 오기
    def btnPath_clicked(self):
        global dirName
        dirName = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Open Data files"), "./",
                                                   QtWidgets.QFileDialog.ShowDirsOnly)
        self.txtFile.setText(str(dirName))

    # 쓰레드 시작
    def start_thread(self):
        # 파일 경로 지정 안 되어 있을 때
        if self.txtFile.text() == "":
            QtWidgets.QMessageBox.warning(self, "", "익명화할 경로를 지정해 주세요.")
            self.btnPath.setFocus()
        else:
            self.thread = ThreadClass(self)
            self.thread.progress.connect(self.update_progress)
            self.thread.start()

    # 진행바 업데이트
    def update_progress(self, progress):
        progress_dict = progress.format_dict
        percentage = (progress_dict['n']) / progress_dict['total'] * 100
        self.progressBar.setValue(percentage)
        progress = str(progress)
        self.statusbar.showMessage(progress)

    # 쓰레드 종료
    def end_process(self):
        QtWidgets.QMessageBox.about(self, "완료", "완료되었습니다.")



    # 종료
    def btnStop_clicked(self):
        sys.exit(0)

class ThreadClass(QtCore.QThread):
    progress = QtCore.Signal(object)

    def __init__(self, parent):
        super(ThreadClass, self).__init__(parent)
        self.parent = parent

    def get_file_list(filePath):
        try:
            list_path = []
            list_file = []
            list_full = []

            for (path, _, file) in os.walk(filePath + '\\'):
                for each_file in file:
                    if each_file[-4:] == '.dcm':
                        list_path.append(path)
                        list_file.append(each_file)
                        list_full.append(os.path.join(os.getcwd(), path, each_file).replace('.\\', ''))
            return list_full
        except:
            return 'get_file_list error.'

    def run(self):
        try:
            t = tqdm(ThreadClass.get_file_list(dirName))
            for filename in t:
                try:
                    Metadata = pydicom.filereader.dcmread(str(filename))
                    self.progress.emit(t)
                    self.sleep(0.1)
                except:
                    return QtWidgets.QMessageBox.warning(self.parent, "", "dicom 파일 읽기 실패")

                try:
                    # anonymizer start
                    Metadata.PatientName = ''
                    Metadata.PatientBirthDate = ''
                    Metadata.PatientSex = ''
                    Metadata.OtherPatientIDs = ''
                    Metadata.PatientAge = ''
                    Metadata.RequestingPhysician = ''
                    Metadata.InstitutionName = ''
                    Metadata.InstitutionAddress = ''
                    Metadata.ReferringPhysicianName = ''
                    Metadata.StationName = ''
                    Metadata.PhysiciansOfRecord = ''
                    Metadata.StudyDate = ''
                    Metadata.SeriesDate = ''
                    Metadata.AcquisitionDate = ''
                    Metadata.ContentDate = ''
                    Metadata.StudyTime = '000000.000000'
                    Metadata.SeriesTime = '000000.000000'
                    Metadata.AcquisitionTime = '000000'
                    Metadata.ContentTime = '000000'
                    Metadata.Manufacturer = ''
                    Metadata.ManufacturerModelName = ''
                    Metadata.DateOfLastCalibration = ''
                    Metadata.TimeOfLastCalibration = ''
                    Metadata.StationName = ''
                    Metadata.OperatorsName = ''
                    Metadata.StudyDescription = ''
                    Metadata.SeriesDescription = ''
                    Metadata.InstitutionalDepartmentName = ''
                    Metadata.ProtocolName = ''

                    Metadata.save_as(str(filename))

                except:
                    return QtWidgets.QMessageBox.warning(self.parent, "", "익명화 실패")
        except:
            return
        finally:
            self.parent.progressBar.setValue(100)
            self.parent.end_process()

    def stop(self):
        self.terminate()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    p = AnonymizeApp()
    p.show()
    app.exec_()