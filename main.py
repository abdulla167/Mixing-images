from PyQt5 import QtWidgets
from output import Ui_MainWindow
import sys
import numpy as np
from PyQt5.QtGui import QPixmap
import qimage2ndarray
from imageModel import ImageModel
from modesEnum import Modes
import logging
logging.basicConfig(filename = "logging.Log", level=logging.DEBUG, filemode='w')
logger = logging.getLogger()


class ApplicationWindow(QtWidgets.QMainWindow):
    slidersValues = np.array([0, 0])
    lastComponent = np.array(["initial_value_max"])
    loaded1 = False
    loaded2 = False

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.open_image_dropMenu = np.array([self.ui.actionimage1, self.ui.actionimage2])
        self.open_image_buttons = np.array([self.ui.Add1, self.ui.Add2])
        self.Sliders = np.array([self.ui.Slider1, self.ui.Slider2])
        self.lineEdit = np.array([self.ui.lineEdit_2, self.ui.lineEdit])
        self.comboboxes2 = np.array([self.ui.comboBox_4, self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7])
        self.comboboxes1 = np.array([self.ui.comboBox, self.ui.comboBox_2])

        for i in range(3):
            self.connect_comboboxes2(i)

        for i in range(2):
            self.connect_open_buttons(i)

        for i in range(2):
            self.connect_open_dropmenu(i)

        for i in range(2):
            self.connect_sliders(i)

        for i in range(2):
            self.connect_comboboxes1(i)

    def connect_comboboxes2(self, i:'int'):
        self.comboboxes2[i].currentIndexChanged.connect(self.get_comboboxes_choices)

    def connect_comboboxes1(self, i:'int'):
        self.comboboxes1[i].currentIndexChanged.connect(lambda: self.display_component(i))

    def connect_sliders(self, i:'int'):
        self.Sliders[i].valueChanged.connect(lambda: self.slider_value(i))

    def connect_open_dropmenu(self, i:'int'):
        self.open_image_dropMenu[i].triggered.connect(lambda: self.get_image(i + 1))

    def connect_open_buttons(self, i:'int'):
        self.open_image_buttons[i].clicked.connect(lambda: self.get_image_path(i + 1))

    def slider_value(self, i:'int'):
        value = self.Sliders[i].value()
        self.lineEdit[i].setText(str(value))
        self.slidersValues[i] = value
        logger.info("user changed slider{} value to {}".format(i+1,value))
        self.get_comboboxes_choices()

    def error_message(self, error_text:'str'):
        logger.warning('Warning: The two images do not have the same size')
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(error_text)
        msg.exec_()

    def get_image_path(self, image_no:'int'):   # function to take a path, making new image object and display the original image
        image_path = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "~", "Images ( *.png *.jpg )")
        logger.info("user loaded image{}".format(image_no))
        if image_path[0] == "":    # check the user cancel the open dialog or selected an image to avoid crash
            pass
        else:
            if image_no == 1:
                self.image1 = ImageModel(image_path[0])
                self.get_image(image_no, self.image1, self.loaded2, self.ui.Image1_display1)
            if image_no == 2:
                self.image2 = ImageModel(image_path[0])
                self.get_image(image_no, self.image2, self.loaded1, self.ui.Image2_display1)

    def get_image(self,image_num:'int', image:'ImageModel',image_exist:'bool', image_display):
        if image_exist:
            if self.image2.imgByte.shape == self.image1.imgByte.shape:
                img = qimage2ndarray.array2qimage(image.imgByte, normalize=True)
                self.ui.Image2_display1.setPixmap(QPixmap(img))
                if image_num == 1:
                    self.loaded1 = True
                else:
                    self.loaded2 = True
            else:
                del image
                logger.info('failed to load image {}'.format(image_num))
                self.error_message("The two images are not equal in size")
        else:
            img = qimage2ndarray.array2qimage(image.imgByte, normalize=True)
            image_display.setPixmap(QPixmap(img))
            if image_num == 1:
                self.loaded1 = True
            else:
                self.loaded2 = True


    # fuction responsible for showing the component of image1 and image2 which user need by calling the function below it
    def display_component(self, combox_num:'int'):
        if combox_num == 0:
            option = self.ui.comboBox.currentText()
            self.display(self.ui.Image1_display2, combox_num, option)
        else:
            option = self.ui.comboBox_2.currentText()
            self.display(self.ui.Image2_display2, combox_num, option)

    def display(self, image_display, combox_num, option:'str'):
        if option == "None":
            image_display.clear()
        elif option == "Magnitude":
            img = qimage2ndarray.array2qimage(self.image1.magnitude, normalize=True)
            image_display.setPixmap(QPixmap(img))
        elif option == "Phase":
            img = qimage2ndarray.array2qimage(self.image1.phase, normalize=True)
            image_display.setPixmap(QPixmap(img))
        elif option == "Real":
            img = qimage2ndarray.array2qimage(self.image1.real, normalize=True)
            image_display.setPixmap(QPixmap(img))
        else:
            img = qimage2ndarray.array2qimage(self.image1.imaginary, normalize=True)
            image_display.setPixmap(QPixmap(img))
        logger.info('user displayed {} component of image{}'.format(option, combox_num + 1))

    def get_comboboxes_choices(self):
        # here we get the combo_boxes string values (components and images the user selected)
        imageOfComponent1 = self.ui.comboBox_4.currentText()
        component1 = self.ui.comboBox_6.currentText()
        imageOfComponent2 = self.ui.comboBox_5.currentText()
        component2 = self.ui.comboBox_7.currentText()
        # update combo-box of component2 based on user choice of component1
        self.update_combobox(component1)
        # get the output combo-box value which the user change to decide he will display on which channel
        output_display = self.ui.comboBox_3.currentText()
        # send them to function to make some if condtions to select what should be send to mix function
        self.choose_output(imageOfComponent1, component1, imageOfComponent2, component2, output_display)

    def choose_output(self, imageOfComponent1:'str', component1:'str', imageOfComponent2:'str', component2:'str', output_display:'str'):
        ratio1 = self.slidersValues[0] / 100
        ratio2 = self.slidersValues[1] / 100
        if self.loaded1 == True and self.loaded2 == True :
            if imageOfComponent1 == "image1" and imageOfComponent2 == "image1":
                output = self.send_to_mix(component1,component2, imageOfComponent1, imageOfComponent2, self.image1, self.image2,ratio1, ratio2)
            elif imageOfComponent1 == "image2" and imageOfComponent2 == "image2":
                output = self.send_to_mix(component1,component2, imageOfComponent1, imageOfComponent2, self.image2, self.image1, ratio1, ratio2)
            elif imageOfComponent1 == "image1" and imageOfComponent2 == "image2":
                output = self.send_to_mix(component1,component2, imageOfComponent1, imageOfComponent2, self.image1, self.image2,ratio1, ratio2)
            elif imageOfComponent1 == "image2" and imageOfComponent2 == "image1":
                output = self.send_to_mix(component1,component2, imageOfComponent1, imageOfComponent2, self.image2, self.image1, ratio1, ratio2)
            else:
                output = np.array([[]])
            self.display_output(output_display, output, component1, imageOfComponent1, component2, imageOfComponent2, ratio1, ratio2)

    # function which send image models and ratios and mode to mixing function depending on the choosen mode by the user
    def send_to_mix(self, component1:'str', component2:'str', imageOfComponent1:'str', imageOfComponent2:'str', image:'ImageModel', imageToBeMixed:'ImageModel', ratio1:'float', ratio2:'float')-> np.ndarray:
        if not (imageOfComponent1 == imageOfComponent2):
            if component1 == "Real":
                mode = Modes.realAndImaginary
                output = image.mixing(imageToBeMixed, ratio1, 1 - ratio2, mode)
            elif component1 == "Imaginary":
                mode = Modes.realAndImaginary
                output = image.mixing(imageToBeMixed, 1 - ratio2, ratio1, mode)
            elif component1 == "Magnitude" :
                if component2 == "Phase":
                    mode = Modes.magnitudeAndPhase
                    output = image.mixing(imageToBeMixed, ratio1, 1 - ratio2, mode)
                elif component2 == "Uniform_Phase":
                    mode = Modes.magnitudeAndUniformPhase
                    output = image.mixing(imageToBeMixed, ratio1, 1 - ratio2, mode)
                else:
                    output = np.array([[]])
            elif component1 == "Phase" :
                if component2 == "Magnitude":
                    mode = Modes.magnitudeAndPhase
                    output = image.mixing(imageToBeMixed, 1 - ratio2, ratio1, mode)
                elif component2 == "Uniform_Magnitude":
                    mode = Modes.uniformMagnitudeAndPhase
                    output = image.mixing(imageToBeMixed, 1 - ratio2, ratio1, mode)
                else:
                    output = np.array([[]])
            elif component1 == "Uniform_Magnitude":
                if component2 == "Phase":
                    mode = Modes.uniformMagnitudeAndPhase
                    output = image.mixing(imageToBeMixed, ratio1, 1 - ratio2, mode)
                elif component2 == "Uniform_Phase":
                    mode = Modes.uniformMagnitudeAndUniformPhase
                    output = imageToBeMixed.mixing(image, ratio1, ratio2, mode)
                else:
                    output = np.array([[]])
            elif component1 == "Uniform_Phase":
                if component2 == "Magnitude":
                    mode = Modes.magnitudeAndUniformPhase
                    output = image.mixing(imageToBeMixed, 1 - ratio2, ratio1, mode)
                elif component2 == "Uniform_Magnitude":
                    mode = Modes.uniformMagnitudeAndUniformPhase
                    output = image.mixing(imageToBeMixed, 1 - ratio2, ratio1, mode)
                else:
                    output = np.array([[]])
            else:
                output = np.array([[]])
        else:
            if component1 == "Real":
                mode = Modes.realAndImaginary
                output = image.mixing(imageToBeMixed, ratio1, ratio2, mode)
            elif component1 == "Imaginary":
                mode = Modes.realAndImaginary
                output = image.mixing(imageToBeMixed, ratio2, ratio1, mode)
            elif component1 == "Magnitude":
                if component2 == "Phase":
                    mode = Modes.magnitudeAndPhase
                    output = image.mixing(imageToBeMixed, ratio1, ratio2, mode)
                elif component2 == "Uniform_Phase":
                    mode = Modes.magnitudeAndUniformPhase
                    output = image.mixing(imageToBeMixed, ratio1, ratio2, mode)
                else:
                    output = np.array([[]])
            elif component1 == "Phase":
                if component2 == "Magnitude":
                    mode = Modes.magnitudeAndPhase
                    output = image.mixing(imageToBeMixed, ratio2, ratio1, mode)
                elif component2 == "Uniform_Magnitude":
                    mode = Modes.uniformMagnitudeAndPhase
                    output = image.mixing(imageToBeMixed, ratio2, ratio1, mode)
                else:
                    output = np.array([[]])
            elif component1 == "Uniform_Magnitude":
                if component2 == "Phase":
                    mode = Modes.uniformMagnitudeAndPhase
                    output = image.mixing(imageToBeMixed, ratio1, ratio2, mode)
                elif component2 == "Uniform_Phase":
                    mode = Modes.uniformMagnitudeAndUniformPhase
                    output = image.mixing(imageToBeMixed, ratio1, ratio2, mode)
                else:
                    output = np.array([[]])
            elif component1 == "Uniform_Phase":
                if component2 == "Magnitude":
                    mode = Modes.magnitudeAndUniformPhase
                    output = image.mixing(imageToBeMixed, ratio2, ratio1, mode)
                elif component2 == "Uniform_Magnitude":
                    mode = Modes.uniformMagnitudeAndUniformPhase
                    output = image.mixing(imageToBeMixed, ratio2, ratio1, mode)
                else:
                    output = np.array([[]])
            else:
                output = np.array([[]])
        return output

    def display_output(self, output_display:'str', output_array:'np.ndarray', component1:'str', image1:'str', component2:'str', image2:'str', ratio1:'float', ratio2:'float'):
        if output_array.size == 0:
            pass
        else:
            logger.info('user mixed {} component of {} with {} component of {} with ratio1={} and ratio2={}'.format(component1, image1, component2, image2, ratio1, ratio2))
            img = qimage2ndarray.array2qimage(output_array, normalize=True)
            if output_display == "output1":
                self.ui.Output1_display.setPixmap(QPixmap(img ))
            else:
                self.ui.Output2_display.setPixmap(QPixmap(img))
            logger.info('output image is displayed on {}'.format(output_display))

    def update_combobox(self, component1:'str'):
        if component1 == self.lastComponent[0]:
            pass
        else:
            self.lastComponent[0] = component1
            self.ui.comboBox_7.clear()
            if component1 == "Magnitude" or component1 == "Uniform_Magnitude":
                self.ui.comboBox_7.addItems(["Phase", "Uniform_Phase"])
            elif component1 == "Phase" or component1 == "Uniform_Phase":
                self.ui.comboBox_7.addItems(["Magnitude", "Uniform_Magnitude"])
            elif component1 == "None":
                self.ui.comboBox_7.addItems(
                    ["None", "Magnitude", "Phase", "Real", "Imaginary", "Uniform_Magnitude", "Uniform_Phase"])
            else:
                if component1 == "Real":
                    self.ui.comboBox_7.addItems(["Imaginary"])
                else:
                    self.ui.comboBox_7.addItems(["Real"])

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
