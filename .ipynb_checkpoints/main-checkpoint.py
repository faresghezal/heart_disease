from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QGroupBox,QRadioButton,QLabel,QSpinBox,QHBoxLayout,QDoubleSpinBox,QMessageBox
import joblib
import pandas as pd


app = QApplication([])
window = QWidget()
mainlayout = QHBoxLayout()
leftlayout = QVBoxLayout()
rightayout = QVBoxLayout()
group1 = QGroupBox("sex")
firstlayout = QVBoxLayout()
sexradioButton1 = QRadioButton("male")
sexradioButton2 = QRadioButton("female")
sexradioButton1.setChecked(True)
firstlayout.addWidget(sexradioButton1)
firstlayout.addWidget(sexradioButton2)
group1.setLayout(firstlayout)    
leftlayout.addWidget(group1)

group2 = QGroupBox("chest pain type")
secondlayout = QVBoxLayout()
chestradioButton1 = QRadioButton("typical")
chestradioButton2 = QRadioButton("typical angina")
chestradioButton3 = QRadioButton("non-anginal pain")
chestradioButton4 = QRadioButton("asymptomatic")
chestradioButton1.setChecked(True)
secondlayout.addWidget(chestradioButton1)
secondlayout.addWidget(chestradioButton2)
secondlayout.addWidget(chestradioButton3)
secondlayout.addWidget(chestradioButton4)
group2.setLayout(secondlayout)    
leftlayout.addWidget(group2)

group3 = QGroupBox("fasting blood sugar")
thirdlayout = QVBoxLayout()
sugarradioButton1 = QRadioButton(" > 120 mg/dl")
sugarradioButton2 = QRadioButton(" < 120 mg/dl")
sugarradioButton1.setChecked(True)
thirdlayout.addWidget(sugarradioButton1)
thirdlayout.addWidget(sugarradioButton2)
group3.setLayout(thirdlayout)    
leftlayout.addWidget(group3)

group4 = QGroupBox("resting ecg")
fourthlayout = QVBoxLayout()
ecgradioButton1 = QRadioButton("normal")
ecgradioButton2 = QRadioButton("Abnormality in ST-T wave")
ecgradioButton3 = QRadioButton(" Left ventricular hypertrophy")
ecgradioButton1.setChecked(True)
fourthlayout.addWidget(ecgradioButton1)
fourthlayout.addWidget(ecgradioButton2)
fourthlayout.addWidget(ecgradioButton3)
group4.setLayout(fourthlayout)    
leftlayout.addWidget(group4)

group5 = QGroupBox("exercise angina")
fifthlayout = QVBoxLayout()
anginaradioButton1 = QRadioButton("NO")
anginaradioButton2 = QRadioButton("YES")
anginaradioButton1.setChecked(True)
fifthlayout.addWidget(anginaradioButton1)
fifthlayout.addWidget(anginaradioButton2)
group5.setLayout(fifthlayout)    
leftlayout.addWidget(group5)

group6 = QGroupBox("ST slope")
sixthlayout = QVBoxLayout()
sloperadioButton1 = QRadioButton("normal")
sloperadioButton2 = QRadioButton("Upsloping")
sloperadioButton3 = QRadioButton("Flat")
sloperadioButton4 = QRadioButton("Downsloping")
sloperadioButton1.setChecked(True)
sixthlayout.addWidget(sloperadioButton1)
sixthlayout.addWidget(sloperadioButton2)
sixthlayout.addWidget(sloperadioButton3)
sixthlayout.addWidget(sloperadioButton4)
group6.setLayout(sixthlayout)    
leftlayout.addWidget(group6)
groupl = QGroupBox()
groupl.setLayout(leftlayout)
mainlayout.addWidget(groupl)


group1_1 = QGroupBox("age")
layout1 = QVBoxLayout()
agespinBox = QSpinBox()
agespinBox.setValue(50)
agespinBox.setRange(20,100)
layout1.addWidget(agespinBox)
group1_1.setLayout(layout1)    
rightayout.addWidget(group1_1)

group1_2 = QGroupBox("resting bp s")
layout2 = QVBoxLayout()
restingspinBox = QSpinBox()
restingspinBox.setValue(100)
restingspinBox.setRange(0,200)
layout2.addWidget(restingspinBox)
group1_2.setLayout(layout2)    
rightayout.addWidget(group1_2)

group1_3 = QGroupBox("cholesterol")
layout3 = QVBoxLayout()
cholesterolspinBox = QSpinBox()
cholesterolspinBox.setValue(100)
cholesterolspinBox.setRange(0,650)
layout3.addWidget(cholesterolspinBox)
group1_3.setLayout(layout3)    
rightayout.addWidget(group1_3)

group1_4 = QGroupBox("max heart rate")
layout4 = QVBoxLayout()
heartspinBox = QSpinBox()
heartspinBox.setValue(100)
heartspinBox.setRange(0,210)
layout4.addWidget(heartspinBox)
group1_4.setLayout(layout4)    
rightayout.addWidget(group1_4)

group1_5 = QGroupBox("oldpeak")
layout5 = QVBoxLayout()
oldpeakspinBox = QDoubleSpinBox()
oldpeakspinBox.setValue(0)
oldpeakspinBox.setDecimals(1) 
oldpeakspinBox.setRange(-3,7)
oldpeakspinBox.setSingleStep(0.1)
layout5.addWidget(oldpeakspinBox)
group1_5.setLayout(layout5)    
rightayout.addWidget(group1_5)

groupr = QGroupBox()
groupr.setLayout(rightayout)
mainlayout.addWidget(groupr)
run =QPushButton('run')
mainlayout.addWidget(run)
window.setLayout(mainlayout)

def on_button_clicked():
    if (sexradioButton1.isChecked()):
        sex=1
    if (sexradioButton2.isChecked()):
        sex=0
    
    if (chestradioButton1.isChecked()):
        chest_pain_type	=1
    if (chestradioButton2.isChecked()):
        chest_pain_type	=2
    if (chestradioButton3.isChecked()):
        chest_pain_type	=3
    if (chestradioButton4.isChecked()):
        chest_pain_type	=4
    
    if (sugarradioButton1.isChecked()):
        fasting_blood_sugar	=1
    if (sugarradioButton2.isChecked()):
        fasting_blood_sugar	=0
    
    if (ecgradioButton1.isChecked()):
        resting_ecg=0
    if (ecgradioButton2.isChecked()):
        resting_ecg=1
    if (ecgradioButton3.isChecked()):
        resting_ecg=2
    
    if (anginaradioButton1.isChecked()):
        exercise_angina=0
    if (anginaradioButton2.isChecked()):
        exercise_angina=1

    if (sloperadioButton1.isChecked()):
        ST_slope=0
    if (sloperadioButton2.isChecked()):
        ST_slope=1
    if (sloperadioButton3.isChecked()):
        ST_slope=2
    if (sloperadioButton4.isChecked()):
        ST_slope=3
    
    age=agespinBox.value() 
    resting_bp_s=restingspinBox.value() 
    cholesterol=cholesterolspinBox.value() 	
    max_heart_rate=heartspinBox.value() 
    oldpeak=oldpeakspinBox.value() 
    model_clone = joblib.load('my_model.pkl')
    Xnew = pd.DataFrame({"age":[age], 'sex':[sex],'chest pain type':[chest_pain_type],'resting bp s':[resting_bp_s],'cholesterol':[cholesterol],'fasting blood sugar':[fasting_blood_sugar],'resting ecg':[resting_ecg],'max heart rate':[max_heart_rate],'exercise angina':[exercise_angina],'oldpeak':[oldpeak],'ST slope':[ST_slope]})
    ynew = model_clone.predict(Xnew)

    if (ynew[0]==0):
        alert = QMessageBox()
        alert.setText('normal result')
        alert.exec()

    if (ynew[0]==1):
        alert = QMessageBox()
        alert.setText('high possibility of heart problems')
        alert.exec()

run.clicked.connect(on_button_clicked)
window.show()
app.exec()

