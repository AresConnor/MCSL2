from json import dumps, loads
from typing import Union
from PyQt5.QtCore import (
    QSize,
    Qt,
    QRect,
    pyqtSignal
)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QSizePolicy,
    QSpacerItem,
    QFrame,
    QAbstractScrollArea,
    QHBoxLayout,
    QVBoxLayout,
    QSlider
)
from os import path as ospath
from qfluentwidgets import (
    BodyLabel,
    CardWidget,
    CheckBox,
    ComboBox,
    HyperlinkButton,
    PrimaryPushButton,
    RadioButton,
    Slider,
    SmoothScrollArea,
    StrongBodyLabel,
    SwitchButton,
    TitleLabel,
    ColorPickerButton,
    PushButton
)
from MCSL2Lib.variables import scrollAreaViewportQss, MCSL2Version


class _SettingsPage(QWidget):
        
    settingsChanged = pyqtSignal(bool)

    def __init__(self):
        
        super().__init__()
        
        self.fileSettings = {}
        self.unSavedSettings = {}
        self.newServerTypeList = ["Default", "Noob", "Extended", "Import"]
        self.downloadSourceList = ["FastMirror", "MCSLAPI"]
        self.saveSameFileExceptionList = ["ask", "overwrite", "stop"]
        self.outputDeEncodingList = ["utf-8", "gbk"]
        self.inputDeEncodingList = ["follow", "utf-8", "gbk"]
        self.themeList = ["auto", "dark", "light"]
        
        self.readSettings()
        print(self.fileSettings['themeColor'])

        self.gridLayout_3 = QGridLayout(self)
        self.gridLayout_3.setObjectName("gridLayout_3")

        spacerItem = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.titleLimitWidget = QWidget(self)
        self.titleLimitWidget.setObjectName("titleLimitWidget")

        self.gridLayout_2 = QGridLayout(self.titleLimitWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.titleLabel = TitleLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")

        self.gridLayout_2.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.subTitleLabel = StrongBodyLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subTitleLabel.sizePolicy().hasHeightForWidth())
        self.subTitleLabel.setSizePolicy(sizePolicy)
        self.subTitleLabel.setTextFormat(Qt.MarkdownText)
        self.subTitleLabel.setObjectName("subTitleLabel")

        self.gridLayout_2.addWidget(self.subTitleLabel, 2, 0, 1, 1)
        self.saveSettingsBtnWidget = QWidget(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveSettingsBtnWidget.sizePolicy().hasHeightForWidth())
        self.saveSettingsBtnWidget.setSizePolicy(sizePolicy)
        self.saveSettingsBtnWidget.setObjectName("saveSettingsBtnWidget")

        self.horizontalLayout = QHBoxLayout(self.saveSettingsBtnWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.saveBtn = PrimaryPushButton(self.saveSettingsBtnWidget)
        self.saveBtn.setObjectName("saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)
        self.giveUpBtn = PushButton(self.saveSettingsBtnWidget)
        self.giveUpBtn.setObjectName("giveUpBtn")

        self.horizontalLayout.addWidget(self.giveUpBtn)
        self.gridLayout_2.addWidget(self.saveSettingsBtnWidget, 0, 1, 2, 1)
        self.gridLayout_3.addWidget(self.titleLimitWidget, 1, 1, 1, 2)
        self.settingsSmoothScrollArea = SmoothScrollArea(self)
        self.settingsSmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.settingsSmoothScrollArea.setFrameShadow(QFrame.Plain)
        self.settingsSmoothScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.settingsSmoothScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.settingsSmoothScrollArea.setWidgetResizable(True)
        self.settingsSmoothScrollArea.setObjectName("settingsSmoothScrollArea")
        
        self.settingsScrollAreaWidgetContents = QWidget()
        self.settingsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 653, 1505))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsScrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.settingsScrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.settingsScrollAreaWidgetContents.setObjectName("settingsScrollAreaWidgetContents")

        self.verticalLayout = QVBoxLayout(self.settingsScrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.serverSettings = CardWidget(self.settingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverSettings.sizePolicy().hasHeightForWidth())
        self.serverSettings.setSizePolicy(sizePolicy)
        self.serverSettings.setMinimumSize(QSize(630, 200))
        self.serverSettings.setMaximumSize(QSize(16777215, 200))
        self.serverSettings.setObjectName("serverSettings")

        self.gridLayout_7 = QGridLayout(self.serverSettings)
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.autoRunLastServer = QWidget(self.serverSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoRunLastServer.sizePolicy().hasHeightForWidth())
        self.autoRunLastServer.setSizePolicy(sizePolicy)
        self.autoRunLastServer.setObjectName("autoRunLastServer")

        self.horizontalLayout_6 = QHBoxLayout(self.autoRunLastServer)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.autoRunLastServerTitle = BodyLabel(self.autoRunLastServer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoRunLastServerTitle.sizePolicy().hasHeightForWidth())
        self.autoRunLastServerTitle.setSizePolicy(sizePolicy)
        self.autoRunLastServerTitle.setObjectName("autoRunLastServerTitle")

        self.horizontalLayout_6.addWidget(self.autoRunLastServerTitle)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.autoRunLastServerSwitchBtn = SwitchButton(self.autoRunLastServer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoRunLastServerSwitchBtn.sizePolicy().hasHeightForWidth())
        self.autoRunLastServerSwitchBtn.setSizePolicy(sizePolicy)
        self.autoRunLastServerSwitchBtn.setChecked(False)
        self.autoRunLastServerSwitchBtn.setObjectName("autoRunLastServerSwitchBtn")

        self.horizontalLayout_6.addWidget(self.autoRunLastServerSwitchBtn)
        self.gridLayout_7.addWidget(self.autoRunLastServer, 1, 0, 1, 4)
        self.serverSettingsTitle = StrongBodyLabel(self.serverSettings)
        self.serverSettingsTitle.setObjectName("serverSettingsTitle")

        self.gridLayout_7.addWidget(self.serverSettingsTitle, 0, 2, 1, 1)
        self.acceptAllMojangEula = QWidget(self.serverSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptAllMojangEula.sizePolicy().hasHeightForWidth())
        self.acceptAllMojangEula.setSizePolicy(sizePolicy)
        self.acceptAllMojangEula.setObjectName("acceptAllMojangEula")

        self.horizontalLayout_7 = QHBoxLayout(self.acceptAllMojangEula)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.acceptAllMojangEulaTitle = BodyLabel(self.acceptAllMojangEula)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptAllMojangEulaTitle.sizePolicy().hasHeightForWidth())
        self.acceptAllMojangEulaTitle.setSizePolicy(sizePolicy)
        self.acceptAllMojangEulaTitle.setObjectName("acceptAllMojangEulaTitle")

        self.horizontalLayout_7.addWidget(self.acceptAllMojangEulaTitle)
        spacerItem3 = QSpacerItem(311, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.acceptAllMojangEulaSwitchBtn = SwitchButton(self.acceptAllMojangEula)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptAllMojangEulaSwitchBtn.sizePolicy().hasHeightForWidth())
        self.acceptAllMojangEulaSwitchBtn.setSizePolicy(sizePolicy)
        self.acceptAllMojangEulaSwitchBtn.setObjectName("acceptAllMojangEulaSwitchBtn")

        self.horizontalLayout_7.addWidget(self.acceptAllMojangEulaSwitchBtn)
        self.gridLayout_7.addWidget(self.acceptAllMojangEula, 2, 0, 1, 4)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 0, 3, 1, 1)
        self.sendStopInsteadOfKill = QWidget(self.serverSettings)
        self.sendStopInsteadOfKill.setObjectName("sendStopInsteadOfKill")

        self.horizontalLayout_8 = QHBoxLayout(self.sendStopInsteadOfKill)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.sendStopInsteadOfKillTitle = BodyLabel(self.sendStopInsteadOfKill)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendStopInsteadOfKillTitle.sizePolicy().hasHeightForWidth())
        self.sendStopInsteadOfKillTitle.setSizePolicy(sizePolicy)
        self.sendStopInsteadOfKillTitle.setObjectName("sendStopInsteadOfKillTitle")

        self.horizontalLayout_8.addWidget(self.sendStopInsteadOfKillTitle)
        spacerItem5 = QSpacerItem(239, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.sendStopInsteadOfKillSwitchBtn = SwitchButton(self.sendStopInsteadOfKill)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendStopInsteadOfKillSwitchBtn.sizePolicy().hasHeightForWidth())
        self.sendStopInsteadOfKillSwitchBtn.setSizePolicy(sizePolicy)
        self.sendStopInsteadOfKillSwitchBtn.setChecked(True)
        self.sendStopInsteadOfKillSwitchBtn.setObjectName("sendStopInsteadOfKillSwitchBtn")

        self.horizontalLayout_8.addWidget(self.sendStopInsteadOfKillSwitchBtn)
        self.gridLayout_7.addWidget(self.sendStopInsteadOfKill, 3, 0, 1, 4)
        self.serverSettingsIndicator = PrimaryPushButton(self.serverSettings)
        self.serverSettingsIndicator.setMinimumSize(QSize(3, 20))
        self.serverSettingsIndicator.setMaximumSize(QSize(3, 20))
        self.serverSettingsIndicator.setText("")
        self.serverSettingsIndicator.setObjectName("serverSettingsIndicator")

        self.gridLayout_7.addWidget(self.serverSettingsIndicator, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.serverSettings)
        self.configureSettings = CardWidget(self.settingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configureSettings.sizePolicy().hasHeightForWidth())
        self.configureSettings.setSizePolicy(sizePolicy)
        self.configureSettings.setMinimumSize(QSize(630, 150))
        self.configureSettings.setMaximumSize(QSize(16777215, 150))
        self.configureSettings.setObjectName("configureSettings")

        self.gridLayout_15 = QGridLayout(self.configureSettings)
        self.gridLayout_15.setObjectName("gridLayout_15")

        self.onlySaveGlobalServerConfig = QWidget(self.configureSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onlySaveGlobalServerConfig.sizePolicy().hasHeightForWidth())
        self.onlySaveGlobalServerConfig.setSizePolicy(sizePolicy)
        self.onlySaveGlobalServerConfig.setObjectName("onlySaveGlobalServerConfig")

        self.horizontalLayout_63 = QHBoxLayout(self.onlySaveGlobalServerConfig)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")

        self.onlySaveGlobalServerConfigTitle = BodyLabel(self.onlySaveGlobalServerConfig)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onlySaveGlobalServerConfigTitle.sizePolicy().hasHeightForWidth())
        self.onlySaveGlobalServerConfigTitle.setSizePolicy(sizePolicy)
        self.onlySaveGlobalServerConfigTitle.setObjectName("onlySaveGlobalServerConfigTitle")

        self.horizontalLayout_63.addWidget(self.onlySaveGlobalServerConfigTitle)
        spacerItem6 = QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem6)
        self.onlySaveGlobalServerConfigSwitchBtn = SwitchButton(self.onlySaveGlobalServerConfig)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onlySaveGlobalServerConfigSwitchBtn.sizePolicy().hasHeightForWidth())
        self.onlySaveGlobalServerConfigSwitchBtn.setSizePolicy(sizePolicy)
        self.onlySaveGlobalServerConfigSwitchBtn.setObjectName("onlySaveGlobalServerConfigSwitchBtn")

        self.horizontalLayout_63.addWidget(self.onlySaveGlobalServerConfigSwitchBtn)
        self.gridLayout_15.addWidget(self.onlySaveGlobalServerConfig, 3, 0, 1, 4)
        self.configureSettingsTitle = StrongBodyLabel(self.configureSettings)
        self.configureSettingsTitle.setObjectName("configureSettingsTitle")

        self.gridLayout_15.addWidget(self.configureSettingsTitle, 0, 2, 1, 1)
        spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem7, 0, 3, 1, 1)
        self.configureSettingsIndicator = PrimaryPushButton(self.configureSettings)
        self.configureSettingsIndicator.setMinimumSize(QSize(3, 20))
        self.configureSettingsIndicator.setMaximumSize(QSize(3, 20))
        self.configureSettingsIndicator.setText("")
        self.configureSettingsIndicator.setObjectName("configureSettingsIndicator")

        self.gridLayout_15.addWidget(self.configureSettingsIndicator, 0, 1, 1, 1)
        self.newServerType = QWidget(self.configureSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newServerType.sizePolicy().hasHeightForWidth())
        self.newServerType.setSizePolicy(sizePolicy)
        self.newServerType.setObjectName("newServerType")

        self.horizontalLayout_64 = QHBoxLayout(self.newServerType)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")

        self.newServerTypeTitle = BodyLabel(self.newServerType)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newServerTypeTitle.sizePolicy().hasHeightForWidth())
        self.newServerTypeTitle.setSizePolicy(sizePolicy)
        self.newServerTypeTitle.setObjectName("newServerTypeTitle")

        self.horizontalLayout_64.addWidget(self.newServerTypeTitle)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem8)
        self.newServerTypeComboBox = ComboBox(self.newServerType)
        self.newServerTypeComboBox.setObjectName("newServerTypeComboBox")

        self.horizontalLayout_64.addWidget(self.newServerTypeComboBox)
        self.gridLayout_15.addWidget(self.newServerType, 2, 0, 1, 4)
        self.verticalLayout.addWidget(self.configureSettings)
        self.downloadSettings = CardWidget(self.settingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadSettings.sizePolicy().hasHeightForWidth())
        self.downloadSettings.setSizePolicy(sizePolicy)
        self.downloadSettings.setMinimumSize(QSize(630, 245))
        self.downloadSettings.setMaximumSize(QSize(16777215, 245))
        self.downloadSettings.setObjectName("downloadSettings")

        self.gridLayout_10 = QGridLayout(self.downloadSettings)
        self.gridLayout_10.setObjectName("gridLayout_10")

        self.downloadSettingsTitle = StrongBodyLabel(self.downloadSettings)
        self.downloadSettingsTitle.setObjectName("downloadSettingsTitle")

        self.gridLayout_10.addWidget(self.downloadSettingsTitle, 0, 2, 1, 1)
        self.alwaysAskSaveDirectory = QWidget(self.downloadSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alwaysAskSaveDirectory.sizePolicy().hasHeightForWidth())
        self.alwaysAskSaveDirectory.setSizePolicy(sizePolicy)
        self.alwaysAskSaveDirectory.setMinimumSize(QSize(0, 60))
        self.alwaysAskSaveDirectory.setMaximumSize(QSize(16777215, 60))
        self.alwaysAskSaveDirectory.setObjectName("alwaysAskSaveDirectory")

        self.gridLayout_14 = QGridLayout(self.alwaysAskSaveDirectory)
        self.gridLayout_14.setObjectName("gridLayout_14")

        spacerItem9 = QSpacerItem(317, 39, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem9, 0, 1, 2, 1)
        self.alwaysAskSaveDirectoryInfo = BodyLabel(self.alwaysAskSaveDirectory)
        self.alwaysAskSaveDirectoryInfo.setObjectName("alwaysAskSaveDirectoryInfo")

        self.gridLayout_14.addWidget(self.alwaysAskSaveDirectoryInfo, 1, 0, 1, 1)
        self.alwaysAskSaveDirectoryCheckBox = CheckBox(self.alwaysAskSaveDirectory)
        self.alwaysAskSaveDirectoryCheckBox.setObjectName("alwaysAskSaveDirectoryCheckBox")

        self.gridLayout_14.addWidget(self.alwaysAskSaveDirectoryCheckBox, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.alwaysAskSaveDirectory, 2, 0, 1, 4)
        self.aria2Thread = QWidget(self.downloadSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aria2Thread.sizePolicy().hasHeightForWidth())
        self.aria2Thread.setSizePolicy(sizePolicy)
        self.aria2Thread.setObjectName("aria2Thread")

        self.horizontalLayout_55 = QHBoxLayout(self.aria2Thread)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")

        self.aria2ThreadTitle = BodyLabel(self.aria2Thread)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aria2ThreadTitle.sizePolicy().hasHeightForWidth())
        self.aria2ThreadTitle.setSizePolicy(sizePolicy)
        self.aria2ThreadTitle.setObjectName("aria2ThreadTitle")

        self.horizontalLayout_55.addWidget(self.aria2ThreadTitle)
        spacerItem10 = QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem10)
        self.aria2ThreadSlider = Slider(self.aria2Thread)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aria2ThreadSlider.sizePolicy().hasHeightForWidth())
        self.aria2ThreadSlider.setSizePolicy(sizePolicy)
        self.aria2ThreadSlider.setMaximumSize(QSize(16777215, 24))
        self.aria2ThreadSlider.setFocusPolicy(Qt.NoFocus)
        self.aria2ThreadSlider.setMinimum(1)
        self.aria2ThreadSlider.setMaximum(16)
        self.aria2ThreadSlider.setSliderPosition(1)
        self.aria2ThreadSlider.setOrientation(Qt.Horizontal)
        self.aria2ThreadSlider.setInvertedAppearance(False)
        self.aria2ThreadSlider.setInvertedControls(False)
        self.aria2ThreadSlider.setTickPosition(QSlider.NoTicks)
        self.aria2ThreadSlider.setTickInterval(1)
        self.aria2ThreadSlider.setObjectName("aria2ThreadSlider")

        self.horizontalLayout_55.addWidget(self.aria2ThreadSlider)
        self.aria2ThreadNum = BodyLabel(self.aria2Thread)
        self.aria2ThreadNum.setObjectName("aria2ThreadNum")

        self.horizontalLayout_55.addWidget(self.aria2ThreadNum)
        self.gridLayout_10.addWidget(self.aria2Thread, 3, 1, 1, 3)
        self.saveSameFileException = QWidget(self.downloadSettings)
        self.saveSameFileException.setObjectName("saveSameFileException")

        self.horizontalLayout_4 = QHBoxLayout(self.saveSameFileException)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.saveSameFileExceptionTitle = BodyLabel(self.saveSameFileException)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveSameFileExceptionTitle.sizePolicy().hasHeightForWidth())
        self.saveSameFileExceptionTitle.setSizePolicy(sizePolicy)
        self.saveSameFileExceptionTitle.setObjectName("saveSameFileExceptionTitle")

        self.horizontalLayout_4.addWidget(self.saveSameFileExceptionTitle)
        spacerItem11 = QSpacerItem(235, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.saveSameFileExceptionToAsk = RadioButton(self.saveSameFileException)
        self.saveSameFileExceptionToAsk.setChecked(True)
        self.saveSameFileExceptionToAsk.setObjectName("saveSameFileExceptionToAsk")

        self.horizontalLayout_4.addWidget(self.saveSameFileExceptionToAsk)
        self.saveSameFileExceptionToOverwrite = RadioButton(self.saveSameFileException)
        self.saveSameFileExceptionToOverwrite.setObjectName("saveSameFileExceptionToOverwrite")

        self.horizontalLayout_4.addWidget(self.saveSameFileExceptionToOverwrite)
        self.saveSameFileExceptionToStop = RadioButton(self.saveSameFileException)
        self.saveSameFileExceptionToStop.setObjectName("saveSameFileExceptionToStop")

        self.horizontalLayout_4.addWidget(self.saveSameFileExceptionToStop)
        self.gridLayout_10.addWidget(self.saveSameFileException, 4, 1, 1, 3)
        self.downloadSource = QWidget(self.downloadSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadSource.sizePolicy().hasHeightForWidth())
        self.downloadSource.setSizePolicy(sizePolicy)
        self.downloadSource.setObjectName("downloadSource")

        self.horizontalLayout_56 = QHBoxLayout(self.downloadSource)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")

        self.downloadSourceTitle = BodyLabel(self.downloadSource)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadSourceTitle.sizePolicy().hasHeightForWidth())
        self.downloadSourceTitle.setSizePolicy(sizePolicy)
        self.downloadSourceTitle.setObjectName("downloadSourceTitle")

        self.horizontalLayout_56.addWidget(self.downloadSourceTitle)
        spacerItem12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem12)
        self.downloadSourceComboBox = ComboBox(self.downloadSource)
        self.downloadSourceComboBox.setObjectName("downloadSourceComboBox")

        self.horizontalLayout_56.addWidget(self.downloadSourceComboBox)
        self.gridLayout_10.addWidget(self.downloadSource, 1, 0, 1, 4)
        self.downloadSettingsIndicator = PrimaryPushButton(self.downloadSettings)
        self.downloadSettingsIndicator.setMinimumSize(QSize(3, 20))
        self.downloadSettingsIndicator.setMaximumSize(QSize(3, 20))
        self.downloadSettingsIndicator.setText("")
        self.downloadSettingsIndicator.setObjectName("downloadSettingsIndicator")

        self.gridLayout_10.addWidget(self.downloadSettingsIndicator, 0, 1, 1, 1)
        spacerItem13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem13, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.downloadSettings)
        self.consoleSettings = CardWidget(self.settingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleSettings.sizePolicy().hasHeightForWidth())
        self.consoleSettings.setSizePolicy(sizePolicy)
        self.consoleSettings.setMinimumSize(QSize(630, 200))
        self.consoleSettings.setMaximumSize(QSize(16777215, 200))
        self.consoleSettings.setObjectName("consoleSettings")

        self.gridLayout_9 = QGridLayout(self.consoleSettings)
        self.gridLayout_9.setObjectName("gridLayout_9")

        spacerItem14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem14, 0, 3, 1, 1)
        self.quickMenu = QWidget(self.consoleSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickMenu.sizePolicy().hasHeightForWidth())
        self.quickMenu.setSizePolicy(sizePolicy)
        self.quickMenu.setObjectName("quickMenu")

        self.horizontalLayout_53 = QHBoxLayout(self.quickMenu)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")

        self.quickMenuTitle = BodyLabel(self.quickMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickMenuTitle.sizePolicy().hasHeightForWidth())
        self.quickMenuTitle.setSizePolicy(sizePolicy)
        self.quickMenuTitle.setObjectName("quickMenuTitle")

        self.horizontalLayout_53.addWidget(self.quickMenuTitle)
        spacerItem15 = QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem15)
        self.quickMenuSwitchBtn = SwitchButton(self.quickMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickMenuSwitchBtn.sizePolicy().hasHeightForWidth())
        self.quickMenuSwitchBtn.setSizePolicy(sizePolicy)
        self.quickMenuSwitchBtn.setChecked(True)
        self.quickMenuSwitchBtn.setObjectName("quickMenuSwitchBtn")

        self.horizontalLayout_53.addWidget(self.quickMenuSwitchBtn)
        self.gridLayout_9.addWidget(self.quickMenu, 4, 0, 1, 4)
        self.consoleSettingsIndicator = PrimaryPushButton(self.consoleSettings)
        self.consoleSettingsIndicator.setMinimumSize(QSize(3, 20))
        self.consoleSettingsIndicator.setMaximumSize(QSize(3, 20))
        self.consoleSettingsIndicator.setText("")
        self.consoleSettingsIndicator.setObjectName("consoleSettingsIndicator")

        self.gridLayout_9.addWidget(self.consoleSettingsIndicator, 0, 1, 1, 1)
        self.consoleSettingsTitle = StrongBodyLabel(self.consoleSettings)
        self.consoleSettingsTitle.setObjectName("consoleSettingsTitle")

        self.gridLayout_9.addWidget(self.consoleSettingsTitle, 0, 2, 1, 1)
        self.inputDeEncoding = QWidget(self.consoleSettings)
        self.inputDeEncoding.setObjectName("inputDeEncoding")

        self.horizontalLayout_5 = QHBoxLayout(self.inputDeEncoding)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.inputDeEncodingTitle = BodyLabel(self.inputDeEncoding)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputDeEncodingTitle.sizePolicy().hasHeightForWidth())
        self.inputDeEncodingTitle.setSizePolicy(sizePolicy)
        self.inputDeEncodingTitle.setObjectName("inputDeEncodingTitle")

        self.horizontalLayout_5.addWidget(self.inputDeEncodingTitle)
        spacerItem16 = QSpacerItem(272, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.inputDeEncodingComboBox = ComboBox(self.inputDeEncoding)
        self.inputDeEncodingComboBox.setObjectName("inputDeEncodingComboBox")

        self.horizontalLayout_5.addWidget(self.inputDeEncodingComboBox)
        self.gridLayout_9.addWidget(self.inputDeEncoding, 2, 0, 1, 4)
        self.outputDeEncoding = QWidget(self.consoleSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputDeEncoding.sizePolicy().hasHeightForWidth())
        self.outputDeEncoding.setSizePolicy(sizePolicy)
        self.outputDeEncoding.setObjectName("outputDeEncoding")

        self.horizontalLayout_54 = QHBoxLayout(self.outputDeEncoding)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")

        self.outputDeEncodingTitle = BodyLabel(self.outputDeEncoding)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputDeEncodingTitle.sizePolicy().hasHeightForWidth())
        self.outputDeEncodingTitle.setSizePolicy(sizePolicy)
        self.outputDeEncodingTitle.setObjectName("outputDeEncodingTitle")

        self.horizontalLayout_54.addWidget(self.outputDeEncodingTitle)
        spacerItem17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem17)
        self.outputDeEncodingComboBox = ComboBox(self.outputDeEncoding)
        self.outputDeEncodingComboBox.setObjectName("outputDeEncodingComboBox")

        self.horizontalLayout_54.addWidget(self.outputDeEncodingComboBox)
        self.gridLayout_9.addWidget(self.outputDeEncoding, 1, 0, 1, 4)
        self.verticalLayout.addWidget(self.consoleSettings)
        self.softwareSettings = CardWidget(self.settingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.softwareSettings.sizePolicy().hasHeightForWidth())
        self.softwareSettings.setSizePolicy(sizePolicy)
        self.softwareSettings.setMinimumSize(QSize(630, 250))
        self.softwareSettings.setMaximumSize(QSize(16777215, 250))
        self.softwareSettings.setObjectName("softwareSettings")

        self.gridLayout_13 = QGridLayout(self.softwareSettings)
        self.gridLayout_13.setObjectName("gridLayout_13")

        spacerItem18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem18, 0, 3, 1, 1)
        self.startOnStartup = QWidget(self.softwareSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startOnStartup.sizePolicy().hasHeightForWidth())
        self.startOnStartup.setSizePolicy(sizePolicy)
        self.startOnStartup.setObjectName("startOnStartup")

        self.horizontalLayout_61 = QHBoxLayout(self.startOnStartup)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")

        self.startOnStartupTitle = BodyLabel(self.startOnStartup)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startOnStartupTitle.sizePolicy().hasHeightForWidth())
        self.startOnStartupTitle.setSizePolicy(sizePolicy)
        self.startOnStartupTitle.setObjectName("startOnStartupTitle")

        self.horizontalLayout_61.addWidget(self.startOnStartupTitle)
        spacerItem19 = QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem19)
        self.startOnStartupSwitchBtn = SwitchButton(self.startOnStartup)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startOnStartupSwitchBtn.sizePolicy().hasHeightForWidth())
        self.startOnStartupSwitchBtn.setSizePolicy(sizePolicy)
        self.startOnStartupSwitchBtn.setObjectName("startOnStartupSwitchBtn")

        self.horizontalLayout_61.addWidget(self.startOnStartupSwitchBtn)
        self.gridLayout_13.addWidget(self.startOnStartup, 5, 0, 1, 4)
        self.softwareSettingsIndicator = PrimaryPushButton(self.softwareSettings)
        self.softwareSettingsIndicator.setMinimumSize(QSize(3, 20))
        self.softwareSettingsIndicator.setMaximumSize(QSize(3, 20))
        self.softwareSettingsIndicator.setText("")
        self.softwareSettingsIndicator.setObjectName("softwareSettingsIndicator")

        self.gridLayout_13.addWidget(self.softwareSettingsIndicator, 0, 1, 1, 1)
        self.softwareSettingsTitle = StrongBodyLabel(self.softwareSettings)
        self.softwareSettingsTitle.setObjectName("softwareSettingsTitle")

        self.gridLayout_13.addWidget(self.softwareSettingsTitle, 0, 2, 1, 1)
        self.theme = QWidget(self.softwareSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme.sizePolicy().hasHeightForWidth())
        self.theme.setSizePolicy(sizePolicy)
        self.theme.setObjectName("theme")

        self.horizontalLayout_62 = QHBoxLayout(self.theme)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")

        self.themeTitle = BodyLabel(self.theme)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeTitle.sizePolicy().hasHeightForWidth())
        self.themeTitle.setSizePolicy(sizePolicy)
        self.themeTitle.setObjectName("themeTitle")

        self.horizontalLayout_62.addWidget(self.themeTitle)
        spacerItem20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem20)
        self.themeComboBox = ComboBox(self.theme)
        self.themeComboBox.setObjectName("themeComboBox")

        self.horizontalLayout_62.addWidget(self.themeComboBox)
        self.gridLayout_13.addWidget(self.theme, 1, 0, 1, 4)
        self.themeColor = QWidget(self.softwareSettings)
        self.themeColor.setObjectName("themeColor")

        self.horizontalLayout_14 = QHBoxLayout(self.themeColor)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        self.themeColorTitle = BodyLabel(self.themeColor)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeColorTitle.sizePolicy().hasHeightForWidth())
        self.themeColorTitle.setSizePolicy(sizePolicy)
        self.themeColorTitle.setObjectName("themeColorTitle")

        self.horizontalLayout_14.addWidget(self.themeColorTitle)
        spacerItem21 = QSpacerItem(449, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem21)
        self.chooseThemeColorBtn = ColorPickerButton(QColor(str(self.fileSettings['themeColor'])), "主题颜色", self.themeColor, enableAlpha=False)
        self.chooseThemeColorBtn.setObjectName("chooseThemeColorBtn")

        self.horizontalLayout_14.addWidget(self.chooseThemeColorBtn)
        self.gridLayout_13.addWidget(self.themeColor, 3, 0, 1, 4)
        self.alwaysRunAsAdministrator = QWidget(self.softwareSettings)
        self.alwaysRunAsAdministrator.setObjectName("alwaysRunAsAdministrator")

        self.horizontalLayout_15 = QHBoxLayout(self.alwaysRunAsAdministrator)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")

        self.alwaysRunAsAdministratorTitle = BodyLabel(self.alwaysRunAsAdministrator)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alwaysRunAsAdministratorTitle.sizePolicy().hasHeightForWidth())
        self.alwaysRunAsAdministratorTitle.setSizePolicy(sizePolicy)
        self.alwaysRunAsAdministratorTitle.setObjectName("alwaysRunAsAdministratorTitle")

        self.horizontalLayout_15.addWidget(self.alwaysRunAsAdministratorTitle)
        spacerItem22 = QSpacerItem(355, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem22)
        self.alwaysRunAsAdministratorSwitchBtn = SwitchButton(self.alwaysRunAsAdministrator)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alwaysRunAsAdministratorSwitchBtn.sizePolicy().hasHeightForWidth())
        self.alwaysRunAsAdministratorSwitchBtn.setSizePolicy(sizePolicy)
        self.alwaysRunAsAdministratorSwitchBtn.setObjectName("alwaysRunAsAdministratorSwitchBtn")

        self.horizontalLayout_15.addWidget(self.alwaysRunAsAdministratorSwitchBtn)
        self.gridLayout_13.addWidget(self.alwaysRunAsAdministrator, 4, 1, 1, 3)
        self.verticalLayout.addWidget(self.softwareSettings)
        self.updateSettings = CardWidget(self.settingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateSettings.sizePolicy().hasHeightForWidth())
        self.updateSettings.setSizePolicy(sizePolicy)
        self.updateSettings.setMinimumSize(QSize(630, 150))
        self.updateSettings.setMaximumSize(QSize(16777215, 150))
        self.updateSettings.setObjectName("updateSettings")

        self.gridLayout_6 = QGridLayout(self.updateSettings)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.currentVer = QWidget(self.updateSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentVer.sizePolicy().hasHeightForWidth())
        self.currentVer.setSizePolicy(sizePolicy)
        self.currentVer.setObjectName("currentVer")

        self.horizontalLayout_48 = QHBoxLayout(self.currentVer)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")

        self.currentVerTitle = BodyLabel(self.currentVer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentVerTitle.sizePolicy().hasHeightForWidth())
        self.currentVerTitle.setSizePolicy(sizePolicy)
        self.currentVerTitle.setObjectName("currentVerTitle")

        self.horizontalLayout_48.addWidget(self.currentVerTitle)
        self.currentVerLabel = BodyLabel(self.currentVer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentVerLabel.sizePolicy().hasHeightForWidth())
        self.currentVerLabel.setSizePolicy(sizePolicy)
        self.currentVerLabel.setObjectName("currentVerLabel")

        self.horizontalLayout_48.addWidget(self.currentVerLabel)
        spacerItem23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem23)
        self.checkUpdateBtn = PrimaryPushButton(self.currentVer)
        self.checkUpdateBtn.setObjectName("checkUpdateBtn")

        self.horizontalLayout_48.addWidget(self.checkUpdateBtn)
        self.gridLayout_6.addWidget(self.currentVer, 2, 0, 1, 4)
        self.checkUpdateOnStart = QWidget(self.updateSettings)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkUpdateOnStart.sizePolicy().hasHeightForWidth())
        self.checkUpdateOnStart.setSizePolicy(sizePolicy)
        self.checkUpdateOnStart.setObjectName("checkUpdateOnStart")

        self.horizontalLayout_47 = QHBoxLayout(self.checkUpdateOnStart)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")

        self.checkUpdateOnStartTitle = BodyLabel(self.checkUpdateOnStart)
        self.checkUpdateOnStartTitle.setObjectName("checkUpdateOnStartTitle")

        self.horizontalLayout_47.addWidget(self.checkUpdateOnStartTitle)
        spacerItem24 = QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem24)
        self.checkUpdateOnStartSwitchBtn = SwitchButton(self.checkUpdateOnStart)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkUpdateOnStartSwitchBtn.sizePolicy().hasHeightForWidth())
        self.checkUpdateOnStartSwitchBtn.setSizePolicy(sizePolicy)
        self.checkUpdateOnStartSwitchBtn.setObjectName("checkUpdateOnStartSwitchBtn")

        self.horizontalLayout_47.addWidget(self.checkUpdateOnStartSwitchBtn)
        self.gridLayout_6.addWidget(self.checkUpdateOnStart, 3, 0, 1, 4)
        self.updateSettingsTitle = StrongBodyLabel(self.updateSettings)
        self.updateSettingsTitle.setObjectName("updateSettingsTitle")

        self.gridLayout_6.addWidget(self.updateSettingsTitle, 0, 2, 1, 1)
        self.updateSettingsIndicator = PrimaryPushButton(self.updateSettings)
        self.updateSettingsIndicator.setMinimumSize(QSize(3, 20))
        self.updateSettingsIndicator.setMaximumSize(QSize(3, 20))
        self.updateSettingsIndicator.setText("")
        self.updateSettingsIndicator.setObjectName("updateSettingsIndicator")

        self.gridLayout_6.addWidget(self.updateSettingsIndicator, 0, 1, 1, 1)
        spacerItem25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem25, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.updateSettings)
        self.about = CardWidget(self.settingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy)
        self.about.setMinimumSize(QSize(630, 250))
        self.about.setMaximumSize(QSize(16777215, 250))
        self.about.setObjectName("about")

        self.gridLayout_5 = QGridLayout(self.about)
        self.gridLayout_5.setObjectName("gridLayout_5")

        spacerItem26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem26, 0, 3, 1, 1)
        self.aboutContentWidget = QWidget(self.about)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutContentWidget.sizePolicy().hasHeightForWidth())
        self.aboutContentWidget.setSizePolicy(sizePolicy)
        self.aboutContentWidget.setObjectName("aboutContentWidget")

        self.gridLayout = QGridLayout(self.aboutContentWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.openSourceCodeRepo = HyperlinkButton(self.aboutContentWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openSourceCodeRepo.sizePolicy().hasHeightForWidth())
        self.openSourceCodeRepo.setSizePolicy(sizePolicy)
        self.openSourceCodeRepo.setObjectName("openSourceCodeRepo")

        self.gridLayout.addWidget(self.openSourceCodeRepo, 1, 2, 1, 1)
        self.generateSysReport = PrimaryPushButton(self.aboutContentWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateSysReport.sizePolicy().hasHeightForWidth())
        self.generateSysReport.setSizePolicy(sizePolicy)
        self.generateSysReport.setObjectName("generateSysReport")
        
        self.gridLayout.addWidget(self.generateSysReport, 1, 3, 1, 1)
        self.joinQQGroup = HyperlinkButton(self.aboutContentWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joinQQGroup.sizePolicy().hasHeightForWidth())
        self.joinQQGroup.setSizePolicy(sizePolicy)
        self.joinQQGroup.setObjectName("joinQQGroup")

        self.gridLayout.addWidget(self.joinQQGroup, 1, 0, 1, 1)
        spacerItem27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem27, 1, 4, 1, 2)
        self.openOfficialWeb = HyperlinkButton(self.aboutContentWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openOfficialWeb.sizePolicy().hasHeightForWidth())
        self.openOfficialWeb.setSizePolicy(sizePolicy)
        self.openOfficialWeb.setObjectName("openOfficialWeb")

        self.gridLayout.addWidget(self.openOfficialWeb, 1, 1, 1, 1)
        self.aboutContent = BodyLabel(self.aboutContentWidget)
        self.aboutContent.setObjectName("aboutContent")

        self.gridLayout.addWidget(self.aboutContent, 0, 0, 1, 6)
        self.gridLayout_5.addWidget(self.aboutContentWidget, 2, 0, 1, 4)
        self.aboutIndicator = PrimaryPushButton(self.about)
        self.aboutIndicator.setMinimumSize(QSize(3, 20))
        self.aboutIndicator.setMaximumSize(QSize(3, 20))
        self.aboutIndicator.setText("")
        self.aboutIndicator.setObjectName("aboutIndicator")

        self.gridLayout_5.addWidget(self.aboutIndicator, 0, 1, 1, 1)
        self.aboutTitle = StrongBodyLabel(self.about)
        self.aboutTitle.setObjectName("aboutTitle")

        self.gridLayout_5.addWidget(self.aboutTitle, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.about)
        spacerItem28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem28)
        self.settingsSmoothScrollArea.setWidget(self.settingsScrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.settingsSmoothScrollArea, 2, 1, 1, 1)

        self.titleLabel.setText("设置")
        self.subTitleLabel.setText("自定义你的MCSL2。")
        self.autoRunLastServerTitle.setText("启动时自动运行上次运行的服务器")
        self.autoRunLastServerSwitchBtn.setText("已关闭")
        self.autoRunLastServerSwitchBtn.setOnText("已开启")
        self.autoRunLastServerSwitchBtn.setOffText("已关闭")
        self.serverSettingsTitle.setText("服务器设置")
        self.acceptAllMojangEulaTitle.setText("创建时自动同意服务器的Eula")
        self.acceptAllMojangEulaSwitchBtn.setText("已关闭")
        self.acceptAllMojangEulaSwitchBtn.setOnText("已开启")
        self.acceptAllMojangEulaSwitchBtn.setOffText("已关闭")
        self.sendStopInsteadOfKillTitle.setText("安全关闭服务器而不是结束进程（慎点）")
        self.sendStopInsteadOfKillSwitchBtn.setText("已开启")
        self.sendStopInsteadOfKillSwitchBtn.setOnText("已开启")
        self.sendStopInsteadOfKillSwitchBtn.setOffText("已关闭")
        self.onlySaveGlobalServerConfigTitle.setText("只保存全局服务器设置")
        self.onlySaveGlobalServerConfigSwitchBtn.setText("已关闭")
        self.onlySaveGlobalServerConfigSwitchBtn.setOnText("已开启")
        self.onlySaveGlobalServerConfigSwitchBtn.setOffText("已关闭")
        self.configureSettingsTitle.setText("新建服务器设置")
        self.newServerTypeTitle.setText("新建服务器引导方式")
        self.downloadSettingsTitle.setText("下载设置")
        self.alwaysAskSaveDirectoryInfo.setText("          不勾选，则保存到MCSL2/Downloads文件夹。")
        self.alwaysAskSaveDirectoryCheckBox.setText("总是询问保存路径")
        self.aria2ThreadTitle.setText("Aria2下载引擎线程数")
        self.saveSameFileExceptionTitle.setText("保存路径存在同名文件的处理")
        self.saveSameFileExceptionToAsk.setText("询问")
        self.saveSameFileExceptionToOverwrite.setText("覆盖")
        self.saveSameFileExceptionToStop.setText("停止")
        self.downloadSourceTitle.setText("下载源")
        self.quickMenuTitle.setText("快捷菜单")
        self.quickMenuSwitchBtn.setText("已开启")
        self.quickMenuSwitchBtn.setOnText("已开启")
        self.quickMenuSwitchBtn.setOffText("已关闭")
        self.consoleSettingsTitle.setText("终端设置")
        self.inputDeEncodingTitle.setText("指令输入编码（优先级低于服务器配置设置）")
        self.outputDeEncodingTitle.setText("控制台输出编码（优先级低于服务器配置设置）")
        self.startOnStartupTitle.setText("开机自启动")
        self.startOnStartupSwitchBtn.setText("已关闭")
        self.startOnStartupSwitchBtn.setOnText("已开启")
        self.startOnStartupSwitchBtn.setOffText("已关闭")
        self.softwareSettingsTitle.setText("软件设置")
        self.themeTitle.setText("主题")
        self.themeColorTitle.setText("主题颜色")
        self.chooseThemeColorBtn.setText("选取颜色")
        self.alwaysRunAsAdministratorTitle.setText("总是以管理员身份运行")
        self.alwaysRunAsAdministratorSwitchBtn.setText("已关闭")
        self.alwaysRunAsAdministratorSwitchBtn.setOnText("已开启")
        self.alwaysRunAsAdministratorSwitchBtn.setOffText("已关闭")
        self.currentVerTitle.setText("当前版本：")
        self.currentVerLabel.setText(MCSL2Version)
        self.checkUpdateBtn.setText("检查更新")
        self.checkUpdateOnStartTitle.setText("启动时自动检查更新")
        self.checkUpdateOnStartSwitchBtn.setText("已关闭")
        self.checkUpdateOnStartSwitchBtn.setOnText("已开启")
        self.checkUpdateOnStartSwitchBtn.setOffText("已关闭")
        self.updateSettingsTitle.setText("更新")
        self.openSourceCodeRepo.setText("打开源码仓库")
        self.generateSysReport.setText("系统报告")
        self.joinQQGroup.setText("加入官方群聊")
        self.openOfficialWeb.setText("打开官网")
        self.aboutContent.setText("MCSL2是一个开源非营利性项目，遵循GNU General Public License Version 3.0开源协议。\n"
                                 "任何人皆可使用MCSL2的源码进行再编译、修改以及发行，\n"
                                 "但必须在相关源代码中以及软件中给出声明，并且二次分发版本的项目名称应与“MCSL2”有\n"
                                 "明显辨识度。\n"
                                 "\n"
                                 "Copyright ©MCSL Team. All right reserved.\n"
                                 "")
        self.aboutTitle.setText("关于")
        self.aria2ThreadSlider.setValue(8)
        self.settingsSmoothScrollArea.viewport().setStyleSheet(scrollAreaViewportQss)
        self.newServerTypeComboBox.addItems(["初始（简易+进阶+导入）", "简易模式", "进阶模式", "导入"])
        self.newServerTypeComboBox.setCurrentIndex(0)
        self.downloadSourceComboBox.addItems(["FastMirror", "MCSLAPI"])
        self.downloadSourceComboBox.setCurrentIndex(0)
        self.aria2ThreadNum.setText(str(self.aria2ThreadSlider.value()))
        self.aria2ThreadSlider.valueChanged.connect(lambda: self.aria2ThreadNum.setText(str(self.aria2ThreadSlider.value())))
        self.outputDeEncodingComboBox.addItems(["UTF-8", "GBK"])
        self.outputDeEncodingComboBox.setCurrentIndex(0)
        self.inputDeEncodingComboBox.addItems(["跟随控制台输出", "UTF-8", "GBK"])
        self.inputDeEncodingComboBox.setCurrentIndex(0)
        self.themeComboBox.addItems(["自动", "深色", "浅色"])
        self.saveBtn.setText("保存")
        self.giveUpBtn.setText("放弃")
        self.themeComboBox.setCurrentIndex(0)
        self.saveSettingsBtnWidget.setVisible(False)
        
        self.settingsChanged.connect(self.saveSettingsBtnWidget.setVisible)
        self.saveBtn.clicked.connect(self.saveSettings)
        self.giveUpBtn.clicked.connect(self.giveUpSettings)

        # serverSettings
        self.autoRunLastServerSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("autoRunLastServer", self.autoRunLastServerSwitchBtn.isChecked()))
        self.acceptAllMojangEulaSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("acceptAllMojangEula", self.acceptAllMojangEulaSwitchBtn.isChecked()))
        self.sendStopInsteadOfKillSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("sendStopInsteadOfKill", self.sendStopInsteadOfKillSwitchBtn.isChecked()))

        # configureSettings
        self.newServerTypeComboBox.currentIndexChanged.connect(lambda: self.changeSettings("newServerType", self.newServerTypeList[self.newServerTypeComboBox.currentIndex()]))
        self.onlySaveGlobalServerConfigSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("onlySaveGlobalServerConfig", self.onlySaveGlobalServerConfigSwitchBtn.isChecked()))

        # downloadSettings
        self.downloadSourceComboBox.currentIndexChanged.connect(lambda: self.changeSettings("downloadSource", self.downloadSourceList[self.downloadSourceComboBox.currentIndex()]))
        self.alwaysAskSaveDirectoryCheckBox.clicked.connect(lambda: self.changeSettings("alwaysAskSaveDirectory", self.alwaysAskSaveDirectoryCheckBox.isChecked()))
        self.aria2ThreadSlider.valueChanged.connect(lambda: self.changeSettings("aria2Thread", self.aria2ThreadSlider.value()))
        self.saveSameFileExceptionToAsk.clicked.connect(lambda: self.changeSettings("saveSameFileException", self.saveSameFileExceptionList[0]))
        self.saveSameFileExceptionToOverwrite.clicked.connect(lambda: self.changeSettings("saveSameFileException", self.saveSameFileExceptionList[1]))
        self.saveSameFileExceptionToStop.clicked.connect(lambda: self.changeSettings("saveSameFileException", self.saveSameFileExceptionList[2]))

        # consoleSettings
        self.outputDeEncodingComboBox.currentIndexChanged.connect(lambda: self.changeSettings("outputDeEncoding", self.outputDeEncodingList[self.outputDeEncodingComboBox.currentIndex()]))
        self.inputDeEncodingComboBox.currentIndexChanged.connect(lambda: self.changeSettings("inputDeEncoding", self.inputDeEncodingList[self.inputDeEncodingComboBox.currentIndex()]))
        self.quickMenuSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("quickMenu", self.quickMenuSwitchBtn.isChecked()))

        # softwareSettings
        self.themeComboBox.currentIndexChanged.connect(lambda: self.changeSettings("theme", self.themeList[self.themeComboBox.currentIndex()]))
        self.chooseThemeColorBtn.colorChanged.connect(lambda: self.changeSettings("themeColor", str(self.chooseThemeColorBtn.color.name())))
        self.alwaysRunAsAdministratorSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("alwaysRunAsAdministrator", self.alwaysRunAsAdministratorSwitchBtn.isChecked()))
        self.startOnStartupSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("startOnStartup", self.startOnStartupSwitchBtn.isChecked()))

        # updateSettings
        self.checkUpdateOnStartSwitchBtn.checkedChanged.connect(lambda: self.changeSettings("checkUpdateOnStart", self.checkUpdateOnStartSwitchBtn.isChecked()))

        self.refreshSettingsInterface()

    def readSettings(self):
        if ospath.exists(r"./MCSL2/MCSL2_Config.json"):
            if ospath.getsize(r"./MCSL2/MCSL2_Config.json") != 0:
                with open(r"./MCSL2/MCSL2_Config.json", "r", encoding="utf-8") as readConfig:
                    # 从文件读取的配置
                    self.fileSettings = loads(readConfig.read())
                    # 多声明一份给修改设置的时候用
                    self.unSavedSettings = self.fileSettings
                    readConfig.close()

    def changeSettings(self, Setting: str, Status: Union[bool, str, int]):
        self.unSavedSettings.update({Setting: Status})
        self.settingsChanged.emit(True)
    
    def giveUpSettings(self):
        self.refreshSettingsInterface()
        self.unSavedSettings = self.fileSettings
        self.settingsChanged.emit(False)
        
        
    def saveSettings(self):
        self.fileSettings.update(self.unSavedSettings)
        self.unSavedSettings = self.fileSettings
        with open(r"./MCSL2/MCSL2_Config.json", "w+", encoding="utf-8") as writeConfig:
            writeConfig.write(dumps(self.fileSettings, indent=4))
            writeConfig.close()
        self.refreshSettingsInterface()
        self.settingsChanged.emit(False)

    def refreshSettingsInterface(self):

        self.readSettings()
        
        # serverSettings
        self.autoRunLastServerSwitchBtn.setChecked(self.fileSettings['autoRunLastServer'])
        self.acceptAllMojangEulaSwitchBtn.setChecked(self.fileSettings['acceptAllMojangEula'])
        self.sendStopInsteadOfKillSwitchBtn.setChecked(self.fileSettings['sendStopInsteadOfKill'])

        # configureSettings
        self.newServerTypeComboBox.setCurrentIndex(self.newServerTypeList.index(self.fileSettings['newServerType']))
        self.onlySaveGlobalServerConfigSwitchBtn.setChecked(self.fileSettings['onlySaveGlobalServerConfig'])

        # downloadSettings
        self.downloadSourceComboBox.setCurrentIndex(self.downloadSourceList.index(self.fileSettings['downloadSource']))
        self.alwaysAskSaveDirectoryCheckBox.setChecked(self.fileSettings['alwaysAskSaveDirectory'])
        self.aria2ThreadSlider.setValue(self.fileSettings['aria2Thread'])
        self.saveSameFileExceptionRadioBtnList = [self.saveSameFileExceptionToAsk, self.saveSameFileExceptionToOverwrite, self.saveSameFileExceptionToStop]
        self.saveSameFileExceptionRadioBtnList[self.saveSameFileExceptionList.index(self.fileSettings['saveSameFileException'])].setChecked(True)

        # consoleSettings
        self.outputDeEncodingComboBox.setCurrentIndex(self.outputDeEncodingList.index(self.fileSettings['outputDeEncoding']))
        self.inputDeEncodingComboBox.setCurrentIndex(self.inputDeEncodingList.index(self.fileSettings['inputDeEncoding']))
        self.quickMenuSwitchBtn.setChecked(self.fileSettings['quickMenu'])

        # softwareSettings
        self.themeComboBox.setCurrentIndex(self.themeList.index(self.fileSettings['theme']))
        self.chooseThemeColorBtn.setColor(self.fileSettings['themeColor'])
        self.alwaysRunAsAdministratorSwitchBtn.setChecked(self.fileSettings['alwaysRunAsAdministrator'])
        self.startOnStartupSwitchBtn.setChecked(self.fileSettings['startOnStartup'])

        # updateSettings
        self.checkUpdateOnStartSwitchBtn.setChecked(self.fileSettings['checkUpdateOnStart'])
