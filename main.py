# -*- coding: utf-8 -*-
"""
chiwenzhen
2016-07-20
@ruijie

"""
import sys
import Tkinter as Tk
from ttk import Notebook
from model import Evaluator, BreastCancerDataSet, CardiotocographyDataSet
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from frame_train import TrainFrame
from frame_test import TestFrame
from frame_learning_curve import LearningCurveFrame
from frame_validation_curve import ValidationCurveFrame
from frame_roc_auc import RocAucFrame
from frame_gridsearchcv import GridSearchCVFrame
from frame_tsne import TSNEFrame
from frame_main_ctg import CardiotocographyMainFrame
from frame_main_bcancer import BreastCancerMainFrame
from frame_features_pair import FeaturesPairFrame
from frame_features_corr import FeaturesCorrFrame
from frame_features_rank import FeaturesRankFrame
from frame_console import ConsoleFrame


class App:
    def __init__(self, root):
        # 数据载入和分类器训练
        bc_dataset = BreastCancerDataSet()
        bc_x_train = bc_dataset.x_train
        bc_y_train = bc_dataset.y_train
        bc_x_test = bc_dataset.x_test
        bc_y_test = bc_dataset.y_test

        ctg_dataset = CardiotocographyDataSet()
        ctg_x_train = ctg_dataset.x_train
        ctg_y_train = ctg_dataset.y_train
        ctg_x_test = ctg_dataset.x_test
        ctg_y_test = ctg_dataset.y_test

        # 初始化UI
        menubar = Tk.Menu(root)  # 添加菜单
        root.config(menu=menubar)
        filemenu = Tk.Menu(menubar)
        filemenu.add_command(label="Exit", command=sys.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        notebook = Notebook(root)  # 添加标签页
        notebook.pack(fill=Tk.BOTH)

        page_0 = Tk.Frame(notebook)
        notebook.add(page_0, text="Main  ")
        notebook_0 = Notebook(page_0)  # 添加子标签页
        notebook_0.pack(fill=Tk.BOTH)
        page_01 = Tk.Frame(notebook_0)
        notebook_0.add(page_01, text="Breast Cancer")
        page_02 = Tk.Frame(notebook_0)
        notebook_0.add(page_02, text="Cardiotocography")
        page_05 = Tk.Frame(notebook_0)
        notebook_0.add(page_05, text="Cardiotocography Features Rank")
        page_04 = Tk.Frame(notebook_0)
        notebook_0.add(page_04, text="Cardiotocography Features Corr")
        page_03 = Tk.Frame(notebook_0)
        notebook_0.add(page_03, text="Cardiotocography Features Pair")
        page_06 = Tk.Frame(notebook_0)
        notebook_0.add(page_06, text="Console Output")

        page_1 = Tk.Frame(notebook)
        notebook.add(page_1, text="Training  ")
        notebook_1 = Notebook(page_1)  # 添加子标签页
        notebook_1.pack(fill=Tk.BOTH)
        page_11 = Tk.Frame(notebook_1)
        notebook_1.add(page_11, text="LR")
        page_12 = Tk.Frame(notebook_1)
        notebook_1.add(page_12, text="SVM")
        page_13 = Tk.Frame(notebook_1)
        notebook_1.add(page_13, text="RF")

        page_2 = Tk.Frame(notebook)
        notebook.add(page_2, text="Testing  ")
        subnotebook_2 = Notebook(page_2)  # 添加子标签页
        subnotebook_2.pack(fill=Tk.BOTH)
        page_21 = Tk.Frame(subnotebook_2)
        subnotebook_2.add(page_21, text="LR")
        page_22 = Tk.Frame(subnotebook_2)
        subnotebook_2.add(page_22, text="SVM")
        page_23 = Tk.Frame(subnotebook_2)
        subnotebook_2.add(page_23, text="RF")

        page_3 = Tk.Frame(notebook)
        notebook.add(page_3, text="Learning Curve")

        page_4 = Tk.Frame(notebook)
        notebook.add(page_4, text="Validation Curve")

        page_5 = Tk.Frame(notebook)
        notebook.add(page_5, text="ROC & AUC")

        page_6 = Tk.Frame(notebook)
        notebook.add(page_6, text="GridSearchCV")

        page_7 = Tk.Frame(notebook)
        notebook.add(page_7, text="t-SNE")

        # 第0页 主页

        console = ConsoleFrame(page_06)
        console.pack(fill=Tk.BOTH)

        bc_eva = Evaluator(scaler=StandardScaler(), pca=PCA(n_components=2), clf=SVC(probability=True, random_state=1))
        BreastCancerMainFrame(page_01, bc_x_train, bc_y_train, bc_x_test, bc_y_test, bc_eva, console).pack(fill=Tk.BOTH)

        ctg_eva = Evaluator(scaler=StandardScaler(), pca=PCA(n_components=2), clf=SVC(probability=True, random_state=1))
        CardiotocographyMainFrame(page_02, ctg_x_train, ctg_y_train, ctg_x_test, ctg_y_test, ctg_eva, console).pack(fill=Tk.BOTH)

        FeaturesPairFrame(page_03, ctg_x_train, ctg_y_train, ctg_x_test, ctg_y_test, ctg_eva, ctg_dataset.df, console).pack(
            fill=Tk.BOTH)

        FeaturesCorrFrame(page_04, ctg_x_train, ctg_y_train, ctg_x_test, ctg_y_test, ctg_eva, ctg_dataset.df, console).pack(
            fill=Tk.BOTH)

        FeaturesRankFrame(page_05, ctg_x_train, ctg_y_train, ctg_x_test, ctg_y_test, ctg_eva, ctg_dataset.df, console).pack(
            fill=Tk.BOTH)



        # # 第1.1页 LR训练
        # clf_lr = CancerEvaluator()
        # TrainFrame(page_11, x_train, y_train, x_test, y_test, clf_lr).pack(fill=Tk.BOTH)
        #
        # # 第1.2页 SVM训练
        # clf_svm = CancerEvaluator(clf=SVC(kernel='rbf', probability=True, random_state=1))
        # TrainFrame(page_12, x_train, y_train, x_test, y_test, clf_svm).pack(fill=Tk.BOTH)
        #
        # # 第1.3页 随机森林训练
        # clf_rf = CancerEvaluator(clf=RandomForestClassifier(n_estimators=50))
        # TrainFrame(page_13, x_train, y_train, x_test, y_test, clf_rf).pack(fill=Tk.BOTH)
        #
        # # 第2.1页 LR测试
        # TestFrame(page_21, x_train, y_train, x_test, y_test, clf_lr).pack(fill=Tk.BOTH)
        #
        # # 第2.2页 SVM测试
        # TestFrame(page_22, x_train, y_train, x_test, y_test, clf_svm).pack(fill=Tk.BOTH)
        #
        # # 第2.3页 随机森林测试
        # TestFrame(page_23, x_train, y_train, x_test, y_test, clf_rf).pack(fill=Tk.BOTH)
        #
        # # 第3页 学习曲线
        # clf_svm = CancerEvaluator(clf=SVC(kernel='rbf', probability=True, random_state=1))
        # LearningCurveFrame(page_3, x_train, y_train, x_test, y_test, clf_svm).pack(fill=Tk.BOTH)
        #
        # # 第4页 验证曲线
        # clf_svm = CancerEvaluator(clf=SVC(kernel='rbf', probability=True, random_state=1))
        # ValidationCurveFrame(page_4, x_train, y_train, x_test, y_test, clf_svm).pack(fill=Tk.BOTH)
        #
        # # 第5页 ROC&AUC
        # clf_svm = CancerEvaluator(clf=SVC(kernel='rbf', probability=True, random_state=1))
        # RocAucFrame(page_5, x_train, y_train, x_test, y_test, clf_svm).pack(fill=Tk.BOTH)
        #
        # # 第6页，GridSearchCV
        # clf_svm = CancerEvaluator(clf=SVC(random_state=1))
        # GridSearchCVFrame(page_6, x_train, y_train, x_test, y_test, clf_svm).pack(fill=Tk.BOTH)
        #
        # # 第7页 t-SNE
        # TSNEFrame(page_7, x_train, y_train, None, None, None).pack(fill=Tk.BOTH)


if __name__ == "__main__":
    master = Tk.Tk()
    master.wm_title("Breast Cancer Evaluation Platform")
    master.geometry('900x750')
    master.iconbitmap("cancer.ico")
    app = App(master)
    master.mainloop()
