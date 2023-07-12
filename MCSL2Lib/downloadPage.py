from PyQt5.QtCore import Qt, QSize, QRect, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QSizePolicy,
    QWidget,
    QFrame,
    QGridLayout,
    QVBoxLayout,
    QSpacerItem
)
from qfluentwidgets import (
    SmoothScrollArea,
    StrongBodyLabel,
    SubtitleLabel,
    TitleLabel,
    PopUpAniStackedWidget,
    Pivot
)
from MCSL2Lib.MCSLAPIParser import FetchDownloadURLThreadFactory
from MCSL2Lib.variables import scrollAreaViewportQss


class _DownloadPage(QWidget):
    def __init__(self):

        super().__init__()

        self.fetchDownloadURLThreadFactory = FetchDownloadURLThreadFactory()
        self.MCSLAPIDownloadUrlDict = {}
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.titleLimitWidget = QWidget(self)
        self.titleLimitWidget.setObjectName("titleLimitWidget")
        self.verticalLayout = QVBoxLayout(self.titleLimitWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = TitleLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.subTitleLabel = StrongBodyLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subTitleLabel.sizePolicy().hasHeightForWidth())
        self.subTitleLabel.setSizePolicy(sizePolicy)
        self.subTitleLabel.setTextFormat(Qt.MarkdownText)
        self.subTitleLabel.setObjectName("subTitleLabel")
        self.verticalLayout.addWidget(self.subTitleLabel)
        self.gridLayout.addWidget(self.titleLimitWidget, 1, 2, 2, 2)
        spacerItem1 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.downloadStackedWidget = PopUpAniStackedWidget(self)
        self.downloadStackedWidget.setObjectName("downloadStackedWidget")
        self.downloadWithFastMirror = QWidget()
        self.downloadWithFastMirror.setObjectName("downloadWithFastMirror")
        self.gridLayout_2 = QGridLayout(self.downloadWithFastMirror)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.coreListSubtitleLabel = SubtitleLabel(self.downloadWithFastMirror)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coreListSubtitleLabel.sizePolicy().hasHeightForWidth())
        self.coreListSubtitleLabel.setSizePolicy(sizePolicy)
        self.coreListSubtitleLabel.setObjectName("coreListSubtitleLabel")
        self.gridLayout_2.addWidget(self.coreListSubtitleLabel, 0, 0, 1, 1)
        self.versionSubtitleLabel = SubtitleLabel(self.downloadWithFastMirror)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionSubtitleLabel.sizePolicy().hasHeightForWidth())
        self.versionSubtitleLabel.setSizePolicy(sizePolicy)
        self.versionSubtitleLabel.setObjectName("versionSubtitleLabel")
        self.gridLayout_2.addWidget(self.versionSubtitleLabel, 0, 1, 1, 1)
        self.buildSubtitleLabel = SubtitleLabel(self.downloadWithFastMirror)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buildSubtitleLabel.sizePolicy().hasHeightForWidth())
        self.buildSubtitleLabel.setSizePolicy(sizePolicy)
        self.buildSubtitleLabel.setObjectName("buildSubtitleLabel")
        self.gridLayout_2.addWidget(self.buildSubtitleLabel, 0, 2, 1, 1)
        self.coreListSmoothScrollArea = SmoothScrollArea(self.downloadWithFastMirror)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coreListSmoothScrollArea.sizePolicy().hasHeightForWidth())
        self.coreListSmoothScrollArea.setSizePolicy(sizePolicy)
        self.coreListSmoothScrollArea.setMinimumSize(QSize(200, 0))
        self.coreListSmoothScrollArea.setMaximumSize(QSize(200, 16777215))
        self.coreListSmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.coreListSmoothScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.coreListSmoothScrollArea.setWidgetResizable(True)
        self.coreListSmoothScrollArea.setObjectName("coreListSmoothScrollArea")
        self.coreListScrollAreaWidgetContents = QWidget()
        self.coreListScrollAreaWidgetContents.setGeometry(QRect(0, 0, 200, 30))
        self.coreListScrollAreaWidgetContents.setObjectName("coreListScrollAreaWidgetContents")
        self.coreListSmoothScrollArea.setWidget(self.coreListScrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.coreListSmoothScrollArea, 1, 0, 1, 1)
        self.versionSmoothScrollArea = SmoothScrollArea(self.downloadWithFastMirror)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionSmoothScrollArea.sizePolicy().hasHeightForWidth())
        self.versionSmoothScrollArea.setSizePolicy(sizePolicy)
        self.versionSmoothScrollArea.setMinimumSize(QSize(160, 0))
        self.versionSmoothScrollArea.setMaximumSize(QSize(160, 16777215))
        self.versionSmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.versionSmoothScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.versionSmoothScrollArea.setWidgetResizable(True)
        self.versionSmoothScrollArea.setObjectName("versionSmoothScrollArea")
        self.versionScrollAreaWidgetContents = QWidget()
        self.versionScrollAreaWidgetContents.setGeometry(QRect(0, 0, 160, 30))
        self.versionScrollAreaWidgetContents.setObjectName("versionScrollAreaWidgetContents")
        self.versionSmoothScrollArea.setWidget(self.versionScrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.versionSmoothScrollArea, 1, 1, 1, 1)
        self.buildScrollArea = SmoothScrollArea(self.downloadWithFastMirror)
        self.buildScrollArea.setMinimumSize(QSize(304, 0))
        self.buildScrollArea.setFrameShape(QFrame.NoFrame)
        self.buildScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.buildScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.buildScrollArea.setWidgetResizable(True)
        self.buildScrollArea.setObjectName("buildScrollArea")
        self.buildScrollAreaWidgetContents = QWidget()
        self.buildScrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 30))
        self.buildScrollAreaWidgetContents.setObjectName("buildScrollAreaWidgetContents")
        self.buildScrollArea.setWidget(self.buildScrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.buildScrollArea, 1, 2, 1, 1)
        self.downloadStackedWidget.addWidget(self.downloadWithFastMirror)
        self.downloadWithMCSLAPI = QWidget()
        self.downloadWithMCSLAPI.setObjectName("downloadWithMCSLAPI")
        self.gridLayout_3 = QGridLayout(self.downloadWithMCSLAPI)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MCSLAPIPivot = Pivot(self.downloadWithMCSLAPI)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MCSLAPIPivot.sizePolicy().hasHeightForWidth())
        self.MCSLAPIPivot.setSizePolicy(sizePolicy)
        self.MCSLAPIPivot.setMinimumSize(QSize(210, 44))
        self.MCSLAPIPivot.setMaximumSize(QSize(16777215, 44))
        self.MCSLAPIPivot.setObjectName("MCSLAPIPivot")
        self.gridLayout_3.addWidget(self.MCSLAPIPivot, 0, 0, 1, 1)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.MCSLAPIStackedWidget = PopUpAniStackedWidget(self.downloadWithMCSLAPI)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MCSLAPIStackedWidget.sizePolicy().hasHeightForWidth())
        self.MCSLAPIStackedWidget.setSizePolicy(sizePolicy)
        self.MCSLAPIStackedWidget.setObjectName("MCSLAPIStackedWidget")
        self.MCSLAPIJava = QWidget()
        self.MCSLAPIJava.setObjectName("MCSLAPIJava")
        self.MCSLAPIStackedWidget.addWidget(self.MCSLAPIJava)
        self.MCSLAPISpigot = QWidget()
        self.MCSLAPISpigot.setObjectName("MCSLAPISpigot")
        self.MCSLAPIStackedWidget.addWidget(self.MCSLAPISpigot)
        self.MCSLAPIPaper = QWidget()
        self.MCSLAPIPaper.setObjectName("MCSLAPIPaper")
        self.MCSLAPIStackedWidget.addWidget(self.MCSLAPIPaper)
        self.MCSLAPIBungeeCord = QWidget()
        self.MCSLAPIBungeeCord.setObjectName("MCSLAPIBungeeCord")
        self.MCSLAPIStackedWidget.addWidget(self.MCSLAPIBungeeCord)
        self.MCSLAPIOfficialCore = QWidget()
        self.MCSLAPIOfficialCore.setObjectName("MCSLAPIOfficialCore")
        self.MCSLAPIStackedWidget.addWidget(self.MCSLAPIOfficialCore)
        self.gridLayout_3.addWidget(self.MCSLAPIStackedWidget, 1, 0, 1, 2)
        self.downloadStackedWidget.addWidget(self.downloadWithMCSLAPI)
        self.gridLayout.addWidget(self.downloadStackedWidget, 3, 2, 1, 1)
        
        self.downloadStackedWidget.setCurrentWidget(self.downloadWithMCSLAPI)
        self.setObjectName("DownloadInterface")

        self.titleLabel.setText("下载")
        self.subTitleLabel.setText("Aria2引擎高速驱动！")
        self.coreListSubtitleLabel.setText("核心列表")
        self.versionSubtitleLabel.setText("游戏版本")
        self.buildSubtitleLabel.setText("构建列表")

        self.coreListSmoothScrollArea.setAttribute(Qt.WA_StyledBackground)
        self.coreListSmoothScrollArea.viewport().setStyleSheet(scrollAreaViewportQss)
        self.versionSmoothScrollArea.viewport().setStyleSheet(scrollAreaViewportQss)
        self.buildScrollArea.viewport().setStyleSheet(scrollAreaViewportQss)
        self.MCSLAPIPivot.addItem(
            routeKey="MCSLAPIJava",
            text="Java环境",
            onClick=lambda: self.MCSLAPIStackedWidget.setCurrentWidget(self.MCSLAPIJava)
        )
        self.MCSLAPIPivot.addItem(
            routeKey="MCSLAPISpigot",
            text="Spigot核心",
            onClick=lambda: self.MCSLAPIStackedWidget.setCurrentWidget(self.MCSLAPISpigot)
        )
        self.MCSLAPIPivot.addItem(
            routeKey="MCSLAPIPaper",
            text="Paper核心",
            onClick=lambda: self.MCSLAPIStackedWidget.setCurrentWidget(self.MCSLAPIPaper)
        )
        self.MCSLAPIPivot.addItem(
            routeKey="MCSLAPIBungeeCord",
            text="BungeeCord代理",
            onClick=lambda: self.MCSLAPIStackedWidget.setCurrentWidget(self.MCSLAPIBungeeCord)
        )
        self.MCSLAPIPivot.addItem(
            routeKey="MCSLAPIOfficialCore",
            text="Vanilla核心",
            onClick=lambda: self.MCSLAPIStackedWidget.setCurrentWidget(self.MCSLAPIOfficialCore)
        )
        self.MCSLAPIPivot.setCurrentItem("MCSLAPIJava")

    def getMCSLAPI(self):
        workThread = self.fetchDownloadURLThreadFactory.create(_singleton=True, finishSlot=self.updateMCSLAPIDownloadUrlDict)
        if workThread.isRunning():
            return
        else:
            workThread.start()
    
    @pyqtSlot(dict)
    def updateMCSLAPIDownloadUrlDict(self, _downloadUrlDict: dict):
        self.MCSLAPIDownloadUrlDict.update(_downloadUrlDict)
        self.getMCSLAPI()

    # @staticmethod
    # def GetDownloadSubWidgetImage(GraphType):
    #     if GraphType == 0:
    #         return QPixmap(":/MCSL2_Icon/JavaIcon.png")
    #     elif GraphType == 1:
    #         return QPixmap(":/MCSL2_Icon/SpigotIcon.png")
    #     elif GraphType == 2:
    #         return QPixmap(":/MCSL2_Icon/PaperIcon.png")
    #     elif GraphType == 3:
    #         return QPixmap(":/MCSL2_Icon/BungeeCordIcon.png")
    #     elif GraphType == 4:
    #         return QPixmap(":/MCSL2_Icon/OfficialCoreIcon.png")
    #     else:
    #         return None