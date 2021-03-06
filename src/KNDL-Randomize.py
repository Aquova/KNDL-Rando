# Program that randomizes Kirby: Nightmare in Dream Land for GBA
# Written by Aquova, 2017-2018
# http://github.com/Aquova/KNDL-Rando

from PyQt5 import QtWidgets
import os, random, sys, hashlib
from mainwindow import Ui_MainWindow

VERSION = '1.1.0'

# Valid byte values for Kirby's ability
abilityValues = ["00","01","02","03","04","05","06","07","08","09","0A","0B","0C",
                "0D","0E","0F","10","11","12","13","14","15","16","17","18"]

# ROM locations of enemy abilities
abilityLocations = ["7417C4", "7429F4", "740C38", "743344", "742A20", "7417F0", "742A4C",
                     "7418A0", "740C64", "740C90", "7418F8", "742B28", "741924", "741950",
                     "740CE8", "740D14", "741A58", "741A84", "740D6C", "740D98", "740DC4"]

# ROM locations of Kirby's palette
kirbyPaletteLocations = ["DC62A", "DC8AA", "DC96C", "DCB2A", "DCBAA", "DD0C4", "DD0E6", "DD23A", "DD306",
                     "E7418", "E745C", "E74A0", "E9D5C", "E9D7E", "E9ED2", "E9F9E", "F997C", "F997C",
                     "F99C0", "F9A04", "FEFFC", "FF01E", "FF172", "FF23E", "108364", "1083A8", "1083EC",
                     "10C260", "10C282", "10C3D6", "10C4A2", "123604", "123648", "12368C", "12A6DC",
                     "12A6FE", "12A852", "12A91E", "137F80", "137FC4", "138008", "13BF44", "13BF66",
                     "13C0BA", "13C186", "149734", "149778", "14D078", "14D09A", "14D1EE", "14D2BA",
                     "150320", "150364", "1503A8", "1517E4", "151806", "15197C", "151A48", "153810",
                     "153854", "153898", "1543E0", "154402", "154600", "15ECE0", "15ED24", "15ED68",
                     "162678", "16269A", "166CE4", "166D06", "166F04", "16FCF0", "16FD34", "16FD78",
                     "172448", "17246A", "1751A0", "1751C2", "175316", "1753E2", "17C3E4", "17C428",
                     "1801E4", "180206", "18035A", "180426", "183F34", "183F78", "183FBC", "1845E8",
                     "18460A", "18464E", "186C7C", "186C9E", "189714", "189736", "196E48", "196E6A",
                     "1A1890", "1A394C", "1A7818", "1A8830", "1A9D94", "1AB300", "1AC5CC", "1AD30C",
                     "1AE878", "1AF444", "1B19EC", "1B3E14", "1B66FC", "1B6E34", "1BC074", "1BE6BE",
                     "1BE8C0", "1BEFF8", "1C051C", "1C7260", "1C9890", "1CC7EC", "1CC82E", "1CF814",
                     "1D4348", "1D60B8", "1D9F20", "1E1F28", "1E1F6A", "1F0074", "1F0096", "1F1F4C",
                     "1F5A34", "1FA7E0", "1FB9D8", "1FDF58", "1FDF9A", "201374", "203BF4", "20D1E4",
                     "218CD4", "21C3D0", "21DEF0", "23F834", "23F988", "23FA54", "23FA98", "2476A0",
                     "2476E4", "24A9FC", "53F4E6", "596D22", "599922", "5BA46E", "5BD09A", "5BF426",
                     "5C220E", "5C4AAA", "5C7452", "5C9B22", "5CCC90", "5CCCD2", "5E2C22", "609D42",
                     "7DB192", "DC9AA", "DCA2A", "DD34A", "E9FE2", "FF282", "10C4E6", "12A962",
                     "13C1CA", "14D2FE", "151A8C", "154644", "166F48", "175426", "18046A", "184692",
                     "1DD060", "1DEF1C", "2055C4", "20831C", "20B3BC", "20C0E8"]

metaKnightLocations = ["226278", "227A60", "2290C0", "22B2AC", "22EB7C", "23118C", "231BDC", "232030",
                       "2352B4", "235BB0", "238BA4", "238BC6", "23AC00", "23AD88", "23E944", "249BAE",
                       "27D826", "2DFFEC", "2E000E", "2E24BC", "2E24DE", "2E692C", "2EA4BC", "2EA758",
                       "2EE490", "2F0660", "2F1A5C", "2F3242"]

metaKnightSwordLocations = ["226298", "227A80", "2290E0", "22B2CC", "22EB9C", "2311AC", "231BFC",
                            "232050", "2352D4", "235BD0", "235BF2", "235C34", "235C76", "238BE6",
                            "23ADA8", "23E964", "27D846", "2E002E", "2E24FE", "2E694C", "2EA4DC",
                            "2EA778", "2EE4B0", "2F0680", "2F1A7C", "2F3262"]

# Palettes need to be in the same order as in the GUI
kirbyPalettes = ["2104BF563F203C18571053084E082A043F543C383718", # Red
                 "2104DF07FF129F121F169F193911D10C5F05F9049104", # Orange
                 "2104FF077F07FF06DD061606B1054C059F047C043604", # Yellow
                 "2104F953F01BCF136D07880606068305FC055A051205", # Green
                 "21047F7F7F721F66BF55FC3C74206D0CA432272EC621", # Cherry
                 "2104F873EF63684FA13A2136C12D6121BF2A1C169805", # Emerald
                 "2104F57F927F0E7F8B7E067EA365E6408D7D2A71875C", # Ocean
                 "2104577F907A2D72EB69615D0151A1402B60294C2838", # Sapphire
                 "21041A7F977EF57D727D4F6CCD05AA383745B338302C", # Grape
                 "21049B4A3B36D82D7425111DCE148B10B41071082F04", # Chocolate
                 "2104FF7F9C7318639452EF3D6B2DE71C10428C312925", # Chalk
                 "2104FF7FFF7F9C731863734EEF3D6B2D5F35BB243718", # Snow
                 "21043146EF3DAD356B2D29250821C6189F0A1F067A05", # Carbon
                 "0000324A1146CE398C314A290821C6184A29E71CA514", # Mirror
                 "00005D635D63784E784EB235EC18E71C7D2D171DF11C", # Stone
                 "0000FF7FFA7FF57F347B6C7A8779E578357911791179", # Ice
                 "0000BD77607460744354435427282728DA48B5449138", # GBA Meta Knight
                 "5325FB417D733C679C5AFB41F841D3397A29F914B410", # KDL3 Pink
                 "494DF06D7C7739739672F06DF061CE4D6A64E564A450", # KDL3 Blue
                 "00003D3FBD14BD14D914D914B20CAD593D3F5B32B925", # Waddle Dee
                 "0000DE7B2A7664756475E16C405C2038D66AEF51083D", # Lololo
                 "0000DE7BDE451C2D1C2DB6186F0C2700F67A306E2861", # Lalala
                 "0000DE7BFF7F7B6FF75E524ACE394A297B6FF75E524A"] # Grayscale

metaKnightPalettes = ["0000397F317E8E6D0C59DE513B39082C1D4C1848133CFF03DF025702FF7F", # Pink
                      "0000397F317E8E6D0C59FF7F7B6F082C5B6FD65A324AFF03DF025702FF7F", # White
                      "0000397F317E8E6D0C59DD20B918082CB2108F084D04FF03DF025702FF7F", # Red
                      "0000397F317E8E6D0C596932092A082CB2108F084D04FF03DF025702FF7F", # Green
                      "21048C318C314B2D8410630C210421042104210421048C316B2DA514EF3D"] # Mirror

metaKnightSwordPalettes = ["0000D25F2D4F6936073212011614D25F", # Green
                           "0000537FCF7A6C7AE77912011614537F", # Blue
                           "0000757AD37970798D6412011614757A", # Purple
                           "00001936B62D5225EF18120116141936", # Brown
                           "00005D6E1D62BC511939120116145D6E", # Pink
                           "0000FF7F7B6FF75E524A12011614FF7F"] # White

# Creating a custom exception, how fancy
class HashError(Exception):
    pass

class KirbyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(KirbyApp, self).__init__(parent)
        self.setupUi(self)
        self.findROMButton.clicked.connect(self.openFile)
        self.randomizeButton.clicked.connect(self.runRandomizer)
        self.title.setText(self.title.text() + VERSION)

        # Fades out starRodCheck if not clicked
        self.starRodCheck.setEnabled(False)
        self.enemyCheck.toggled.connect(self.starRodCheck.setEnabled)
        self.enemyCheck.toggled.connect(
            lambda checked: not checked and self.starRodCheck.setChecked(False))

        # If noAbilitiesCheck is clicked, enemyCheck is disabled
        self.noAbilitiesCheck.setEnabled(True)
        self.enemyCheck.toggled.connect(self.noAbilitiesCheck.setDisabled)
        self.enemyCheck.toggled.connect(
            lambda checked: checked and self.noAbilitiesCheck.setChecked(False))

        # If enemyCheck is clicked, noAbilitiesCheck is disabled
        self.enemyCheck.setEnabled(True)
        self.noAbilitiesCheck.toggled.connect(self.enemyCheck.setDisabled)
        self.noAbilitiesCheck.toggled.connect(
            lambda checked: checked and self.enemyCheck.setChecked(False))

    # Opens ROM selector window, clears the previous path text
    def openFile(self):
        self.romDisplay.clear()
        self.romFile = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", os.path.dirname(__file__), "GBA ROMs (*.gba)")[0]
        if self.romFile:
            self.romDisplay.setText(self.romFile)

    def getKirbyColor(self):
        c = self.kirbyComboBox.currentIndex()
        if c == (len(kirbyPalettes) + 1):
            return random.randint(0, len(kirbyPalettes)-1)
        return (c - 1)

    def getMKColor(self):
        c = self.MKcomboBox.currentIndex()
        if c == (len(metaKnightPalettes) + 1):
            return random.randint(0, len(metaKnightPalettes)-1)
        return (c - 1)

    def getSwordColor(self):
        c = self.swordComboBox.currentIndex()
        if c == (len(metaKnightSwordPalettes) + 1):
            return random.randint(0, len(metaKnightSwordPalettes)-1)
        return (c - 1)

    def runRandomizer(self):
        try:
            rom = open(self.romFile, 'rb').read()
            testHash = hashlib.md5(rom).hexdigest()
            # Checks for the correct ROM
            if testHash != "35ae64b0f27e60107c14ab956f6cdf70":
                raise HashError("Invalid checksum")
            romList = list(rom)

            # Uses given input as seed, else randomly picks a new seed to use
            KNDL_seed = self.seedValue.text()
            if KNDL_seed == "":
                KNDL_seed = random.randint(0, 999999999)
            random.seed(KNDL_seed)

            if self.enemyCheck.isChecked():
                if self.starRodCheck.isChecked():
                    abilityValues.append("19")

                # Gives enemies new abilities based on random selection from file
                for item in abilityLocations:
                    address = int(item, 16)
                    new_enemy = random.choice(abilityValues)
                    new_enemy = int(new_enemy,16)
                    romList[address] = new_enemy

            elif self.noAbilitiesCheck.isChecked():
                for item in abilityLocations:
                    address = int(item, 16)
                    romList[address] = 0 # Every enemy should be given the "0x00" value, or no ability

            if self.kirbyComboBox.currentIndex() != 0:
                new_color = self.getKirbyColor()
                row = kirbyPalettes[new_color]
                new_colors = []
                for i in range(0, len(row), 2):
                    new_colors.append(int(row[i:i+2],16))

                # Replaces old color palettes with the new
                for item in kirbyPaletteLocations:
                    color_address = int(item, 16)
                    for i in range(0, len(new_colors)):
                        romList[color_address + i] = new_colors[i]

                # Want to change the color of the life icon to match
                # TODO: Someday make this nicer
                romList[int("5A56F2", 16)] = new_colors[0] # 16th byte - Outline
                romList[int("5A56F3", 16)] = new_colors[1]
                romList[int("5A56EE", 16)] = new_colors[4] # 14th byte - Main body
                romList[int("5A56EF", 16)] = new_colors[5]
                romList[int("5A56EA", 16)] = new_colors[12] # 12th byte - Body highlight
                romList[int("5A56EB", 16)] = new_colors[13]
                romList[int("5A56D8", 16)] = new_colors[18] # 3rd byte - Feet
                romList[int("5A56D9", 16)] = new_colors[19]

                # Changing the life icon also messes with the health bar palette, so that needs to be changed too
                romList[int("5A56D6", 16)] = new_colors[20]
                romList[int("5A56D7", 16)] = new_colors[21]
                romList[int("5A56DA", 16)] = new_colors[16]
                romList[int("5A56DB", 16)] = new_colors[17]
                romList[int("5A56DC", 16)] = new_colors[16]
                romList[int("5A56DD", 17)] = new_colors[17]

            if self.MKcomboBox.currentIndex() != 0:
                new_color = self.getMKColor()
                row = metaKnightPalettes[new_color]
                new_colors = []
                for i in range(0, len(row), 2):
                    new_colors.append(int(row[i:i+2],16))

                # Replaces old color palettes with the new
                for item in metaKnightLocations:
                    color_address = int(item, 16)
                    for i in range(0, len(new_colors)):
                        romList[color_address + i] = new_colors[i]

            if self.swordComboBox.currentIndex() != 0:
                new_color = self.getSwordColor()
                row = metaKnightSwordPalettes[new_color]
                new_colors = []
                for i in range(0, len(row), 2):
                    new_colors.append(int(row[i:i+2],16))

                # Replaces old color palettes with the new
                for item in metaKnightSwordLocations:
                    color_address = int(item, 16)
                    for i in range(0, len(new_colors)):
                        romList[color_address + i] = new_colors[i]

            rom = bytes(romList)
            new_rom = open('.'.join(self.romFile.split(".")[:-1]) + "_" + str(KNDL_seed) + ".gba", 'wb')
            new_rom.write(rom)
            new_rom.close()

            QtWidgets.QMessageBox.about(self, "Success", "Your copy of Nightmare in Dream Land has been randomized. Enjoy!")
        except AttributeError:
            QtWidgets.QMessageBox.about(self, "Error", "Error: Specify a ROM location")
        except FileNotFoundError:
            QtWidgets.QMessageBox.about(self, "Error", "Error: File not found")
        except HashError:
            QtWidgets.QMessageBox.about(self, "Error", "The given file is invalid. Please use a US GBA Kirby: Nightmare in Dream Land ROM.")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "Error", "Some mysterious error has occurred. Please contact the developers with information about what happened. {}".format(e))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = KirbyApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
