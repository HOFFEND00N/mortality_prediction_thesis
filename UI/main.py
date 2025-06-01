import sys
import numpy as np
import joblib
from catboost import CatBoostClassifier
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel

model = CatBoostClassifier()
model.load_model(r"../../diplom_synthetic_data_generation/models/model_CatBoost_synthetic_edge_cases_arf.cbm")
scaler = joblib.load(r"../../diplom_synthetic_data_generation/scaler.save")

class MortalityProbabilityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Probability of mortality")

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.fields = {
            'Age': QLineEdit(),
            'Anemia': QLineEdit(),
            'Ejection fraction ': QLineEdit(),
            'Cerebrovascular disease': QLineEdit(),
            'Peripheral artery disease': QLineEdit(),
            'Aortic stenosis': QLineEdit(),
            'Single vessel disease': QLineEdit(),
            'Calcification': QLineEdit(),
            'Stent type - Calipso': QLineEdit(),
            'Medina: side branch': QLineEdit(),
            'Atrial fibrillation': QLineEdit(),
            'Height': QLineEdit(),
            'DEFINITION score (LM)': QLineEdit(),
            'History of cancer': QLineEdit(),
            'Clinical presentation': QLineEdit(),
            'Previous PCI': QLineEdit(),
            'CTO bifurcation': QLineEdit(),
            'SB diameter': QLineEdit(),
            'Trifurcation': QLineEdit(),
            'Dyslipidemia': QLineEdit(),
            'Smoking': QLineEdit(),
            'Restenosis reocclusion': QLineEdit(),
            # 'CKD': QLineEdit(),
            # 'COPD': QLineEdit(),
            # 'Synergy stent type': QLineEdit(),
            # 'History of myocardial infarction': QLineEdit(),
            # 'Stent legnth': QLineEdit(),
            # 'Unstable Angina': QLineEdit(),
            # 'Definitions score': QLineEdit(),
            # 'Side branch dolatation': QLineEdit(),
            # 'LAD/DA': QLineEdit(),
            # 'Stent number 1': QLineEdit(),
            # 'Main branch predilatation': QLineEdit(),
            # 'Side branch predilatation': QLineEdit(),
            # 'Main branch vessel diameter': QLineEdit(),
        }

        for i in self.fields.values():
            i.setText('0')

        for field, widget in self.fields.items():
            self.form_layout.addRow(field, widget)

        self.layout.addLayout(self.form_layout)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_probability)
        self.layout.addWidget(self.calculate_button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def calculate_probability(self):
        global model
        features = np.array([[float(widget.text()) for field, widget in self.fields.items()]])
        print(features)
        features = scaler.transform(features)
        
        # Use CatBoost's predict_proba method which directly returns probability estimates
        proba = model.predict_proba(features)
        
        # CatBoost returns probabilities for all classes, get the probability for class 1 (mortality)
        probability = proba[0][1]
        self.result_label.setText(f"Probability of mortality: {probability * 100:.2f}%")
        
app = QApplication(sys.argv)
window = MortalityProbabilityApp()
window.show()
sys.exit(app.exec_())