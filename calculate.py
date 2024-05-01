from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/Downloads/cis1051/Final')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        income = int(request.form['income'])
        age1619 = int(request.form['age1619'])
        age1923 = int(request.form['age1923'])
        age2370 = int(request.form['age2370'])
        age70Co = int(request.form['age70Co'])
        age70 = int(request.form['age70'])
        selected_sp = request.form.get('sp')
        selected_70 = request.form.get('sp70')
        selected_student = request.form.get('student')
        selected_single = request.form.get('single')
        selected_widow = request.form.get('widow')
        disability = int(request.form['disability'])
        Sdisability = int(request.form['Sdisability'])
        SdisabilityCo = int(request.form['SdisabilityCo'])
        selected_welfare = request.form.get('welfare')
        medical = int(request.form['medical'])
        lifeInsurance = int(request.form.get('life'))
        nurseInsurance = int(request.form.get('nurse'))
        pensionInsurance = int(request.form.get('pension'))
        socialInsurance = int(request.form['social'])
        earthquakeInsurance = int(request.form['earth'])

        total_income = calculate_total_income(income)
        income_deduction = basicDeduction_forIncomeTax(total_income, 0)
        income_deduction = dependentDeduction_forIncomeTax(age1619, age1923, age2370, age70Co, age70, income_deduction)
        income_deduction = spouseDeduction_forIncomeTax(selected_sp, selected_70, income_deduction, total_income)
        income_deduction = studentDeduction_forIncomeTax(selected_student, total_income, income_deduction)
        income_deduction = singleDeduction_forIncomeTax(selected_single, selected_widow, total_income, income_deduction)
        income_deduction = widowDeduction_forIncomeTax(selected_widow, selected_single, total_income, income_deduction)
        income_deduction = disabilityDeduction_forIncomeTax(disability, Sdisability, SdisabilityCo, income_deduction)
        income_deduction = medicalDeduction_forIncomeTax(medical, income_deduction, total_income)
        income_deduction = lifeInsuranceDeduction_forIncomeTax(lifeInsurance, nurseInsurance, pensionInsurance, income_deduction)
        income_deduction = socialInsuranceDeduction_forIncomeTax(socialInsurance, income_deduction)
        income_deduction = earthquakeInsuranceDeduction_forIncomeTax(earthquakeInsurance, income_deduction)
        income_tax = calculate_finalIncomeTax(total_income, income_deduction)

        income_deduction = basicDeduction_forResidentTax(total_income, 0)
        income_deduction = dependentDeduction_forResidentTax(age1619, age1923, age2370, age70Co, age70, income_deduction)
        income_deduction = spouseDeduction_forResidentTax(selected_sp, selected_70, income_deduction, total_income)
        income_deduction = studentDeduction_forResidentTax(selected_student, total_income, income_deduction)
        income_deduction = singleDeduction_forResidentTax(selected_single, selected_widow, total_income, income_deduction)
        income_deduction = widowDeduction_forResidentTax(selected_widow, selected_single, total_income, income_deduction)
        income_deduction = disabilityDeduction_forResidentTax(disability, Sdisability, SdisabilityCo, income_deduction)
        income_deduction = medicalDeduction_forResidentTax(medical, income_deduction, total_income)
        income_deduction = lifeInsuranceDeduction_forResidentTax(lifeInsurance, nurseInsurance, pensionInsurance, income_deduction)
        income_deduction = socialInsuranceDeduction_forResidentTax(socialInsurance, income_deduction)
        income_deduction = earthquakeInsuranceDeduction_forResidentTax(earthquakeInsurance, income_deduction)
        resident_tax = calculate_finalResidentTax(income, total_income, income_deduction, selected_sp, selected_welfare, selected_single, selected_widow, disability, Sdisability)
        
        result = calculate_total_tax(income, income_tax, resident_tax)
        return redirect(url_for('results', total_tax=result['total_tax'], income_tax=result['income_tax'], resident_tax=result['resident_tax']))
    else:
        return render_template('index.html')
    
@app.route('/results')
def results():
    total_tax = request.args.get('total_tax')
    income_tax = request.args.get('income_tax')
    resident_tax = request.args.get('resident_tax')
    return render_template('results.html', total_tax=total_tax, income_tax=income_tax, resident_tax=resident_tax)

@app.route('/article.html')
def article():
    return render_template('article.html')

def calculate_total_income(income):
    if income <= 1625000:
        total_income = income - 550000
    elif income <= 1800000:
        total_income = income - ((income*0.4) - 100000)
    elif income <= 3600000:
        total_income = income - ((income*0.3) + 80000)
    elif income <= 6600000:
        total_income = income - ((income*0.2) + 440000)
    elif income <= 8500000:
        total_income = income - ((income*0.1) + 1100000)
    elif income >= 8500001:
        total_income = income - 1950000
    return total_income


#Calculate Income Tax From Here
def basicDeduction_forIncomeTax(total_income, income_deduction):
    #income_deduction = 0を消した
    if total_income <= 2400000:
        income_deduction += 480000
    elif total_income <= 24500000:
        income_deduction += 320000
    elif total_income <= 25000000:
        income_deduction += 160000
    elif total_income >= 25000001:
        income_deduction += 0
    return income_deduction

def dependentDeduction_forIncomeTax(age1619, age1923, age2370, age70Co, age70, income_deduction):
    if age1619 >= 1:
        income_deduction += 380000 * age1619
    elif age1923 >= 1:
        income_deduction += 630000 * age1923
    elif age2370 >= 1:
        income_deduction += 380000 * age2370
    elif age70Co >= 1:
        income_deduction += 580000 * age70Co
    elif age70 >= 1:
        income_deduction += 480000 * age70
    return income_deduction

def spouseDeduction_forIncomeTax(selected_sp, selected_70, income_deduction, total_income):
    if selected_sp == 'nosp':
        income_deduction += 0
    elif selected_sp == 'spna' or total_income > 10000000:
        income_deduction += 0
    elif selected_sp == 'sp48':
        if selected_70 == 'spUnder70':
            if total_income <= 9000000:
                income_deduction += 380000
            elif total_income <= 9500000:
                income_deduction += 260000
            elif total_income <= 10000000:
                income_deduction += 130000
        elif selected_70 == 'sp70Plus':
            if total_income <= 9000000:
                income_deduction += 480000
            elif total_income <= 9500000:
                income_deduction += 320000
            elif total_income <= 10000000:
                income_deduction += 160000
    elif selected_sp == 'sp95' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 380000
        elif total_income <= 9500000:
            income_deduction += 280000
        elif total_income <= 10000000:
                income_deduction += 130000
    elif selected_sp == 'sp100' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 360000
        elif total_income <= 9500000:
            income_deduction += 240000
        elif total_income <= 10000000:
            income_deduction += 120000
    elif selected_sp == 'sp105' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 310000
        elif total_income <= 9500000:
            income_deduction += 210000
        elif total_income <= 10000000:
            income_deduction += 110000
    elif selected_sp == 'sp110' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 210000
        elif total_income <= 9500000:
            income_deduction += 140000
        elif total_income <= 10000000:
            income_deduction += 70000
    elif selected_sp == 'sp115' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 210000
        elif total_income <= 9500000:
            income_deduction += 140000
        elif total_income <= 10000000:
            income_deduction += 70000
    elif selected_sp == 'sp120' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 160000
        elif total_income <= 9500000:
            income_deduction += 110000
        elif total_income <= 10000000:
            income_deduction += 60000
    elif selected_sp == 'sp125' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 110000
        elif total_income <= 9500000:
            income_deduction += 80000
        elif total_income <= 10000000:
            income_deduction += 40000
    elif selected_sp == 'sp130' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 60000
        elif total_income <= 9500000:
            income_deduction += 40000
        elif total_income <= 10000000:
            income_deduction += 20000
    elif selected_sp == 'sp133' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 30000
        elif total_income <= 9500000:
            income_deduction += 20000
        elif total_income <= 10000000:
            income_deduction += 10000
    return income_deduction
        
def studentDeduction_forIncomeTax(selected_student, total_income, income_deduction):
    if selected_student == 'student' and total_income <= 750000:
            income_deduction += 270000
    else:
        income_deduction += 0
    return income_deduction

def singleDeduction_forIncomeTax(selected_single, selected_widow, total_income, income_deduction):
    if selected_single == 'single':
        if total_income <= 5000000:
            if selected_widow == 'widow': #if both single and widow applicable, apply single parent deduction
                income_deduction += 350000
            elif selected_widow == 'nonwidow':
                income_deduction += 350000
        elif total_income > 5000000:
            income_deduction += 0
    elif selected_single == 'nonsingle':
        income_deduction += 0
    return income_deduction

def widowDeduction_forIncomeTax(selected_widow, selected_single, total_income, income_deduction):
    if selected_widow == 'widow': 
        if selected_single == 'nonsingle' and total_income <= 5000000:
            income_deduction += 270000
        elif total_income > 5000000:
            income_deduction += 0
    elif selected_widow == 'nonwidow':
        income_deduction += 0
    return income_deduction

def disabilityDeduction_forIncomeTax(disability, Sdisability, SdisabilityCo, income_deduction):
    if disability >= 1:
        income_deduction += 270000 * disability
    if Sdisability >= 1:
        income_deduction += 400000 * Sdisability
    if SdisabilityCo >= 1:
        income_deduction += 750000 * SdisabilityCo
    return income_deduction

def medicalDeduction_forIncomeTax(medical, income_deduction, total_income):
    if medical >= 1 and total_income < 2000000:
        income_deduction += medical - total_income * 0.05
    elif medical <= 100000 and total_income >= 2000000:
        income_deduction += 0
    elif 100000 < medical <=2000000 and total_income >= 2000000:
        income_deduction += (medical - 100000)
    elif medical > 2100000 and total_income >= 2000000:
        income_deduction += 2000000
    return income_deduction

def lifeInsuranceDeduction_forIncomeTax(lifeInsurance, nurseInsurance, pensionInsurance, income_deduction):
    if lifeInsurance > 0:
        if lifeInsurance <= 20000:
            income_deduction += lifeInsurance
        elif 20000 < lifeInsurance <= 40000:
            income_deduction += (lifeInsurance * 1/2) + 10000
        elif 40000 < lifeInsurance <= 80000:
            income_deduction += (lifeInsurance * 1/4) + 20000
        elif lifeInsurance > 80000:
            income_deduction += 40000
    if nurseInsurance > 0:
        if nurseInsurance <= 20000:
            income_deduction += nurseInsurance
        elif 20000 < nurseInsurance <= 40000:
            income_deduction += (nurseInsurance * 1/2) + 10000
        elif 40000 < nurseInsurance <= 80000:
            income_deduction += (nurseInsurance * 1/4) + 20000
        elif nurseInsurance > 80000:
            income_deduction += 40000
    if pensionInsurance > 0:
        if pensionInsurance <= 25000:
            income_deduction += pensionInsurance
        elif 25000 < pensionInsurance <= 50000:
            income_deduction += (pensionInsurance * 1/2) + 12500
        elif 50000 < pensionInsurance <= 100000:
            income_deduction += (pensionInsurance * 1/4) + 25000
        elif pensionInsurance > 100000:
            income_deduction += 50000
    return income_deduction

def socialInsuranceDeduction_forIncomeTax(socialInsurance, income_deduction):
    if socialInsurance >= 1:
        income_deduction += socialInsurance
    elif socialInsurance == 0:
        income_deduction += 0
    return income_deduction

def earthquakeInsuranceDeduction_forIncomeTax(earthquakeInsurance, income_deduction):
    if earthquakeInsurance >= 1:
        if earthquakeInsurance > 50000:
            income_deduction += 50000
        elif earthquakeInsurance <= 50000:
            income_deduction += earthquakeInsurance
    elif earthquakeInsurance == 0:
        income_deduction += 0
    return income_deduction

def calculate_finalIncomeTax(total_income, income_deduction):
    taxable_income = ((total_income - income_deduction)//1000) * 1000  #taxable income must be rounded off
    
    standard_income_tax, income_tax = 0, 0

    #apply tax deduction and calculate standard income tax 
    if taxable_income <= 1950000:
        standard_income_tax = taxable_income * 0.05
    elif 1950000 < taxable_income <= 3300000:
        standard_income_tax = (taxable_income * 0.1) - 97500
    elif 3300000 < taxable_income <= 6950000:
        standard_income_tax = (taxable_income * 0.2) - 427500
    elif 6950000 < taxable_income <= 9000000:
        standard_income_tax = (taxable_income * 0.23) - 636000
    elif 9000000 < taxable_income <= 18000000:
        standard_income_tax = (taxable_income * 0.33) - 1536000
    elif 18000000 < taxable_income <= 4000000:
        standard_income_tax = (taxable_income * 0.4) - 2796000
    elif 40000000 < taxable_income:
        standard_income_tax = (taxable_income * 0.45) - 4796000

    #calculate final income tax by adding reconstruction income tax
    income_tax += ((standard_income_tax + (standard_income_tax * 0.021)) // 100 ) * 100
    
    return income_tax
#Calculate Income Tax End Here


#Calculate Resident Tax From Here
def basicDeduction_forResidentTax(total_income, income_deduction):
    if total_income <= 24000000:
        income_deduction += 430000
    elif total_income <= 24500000:
        income_deduction += 290000
    elif total_income <= 25000000:
        income_deduction += 150000
    elif total_income > 25000000:
        income_deduction += 0
    return income_deduction

def dependentDeduction_forResidentTax(age1619, age1923, age2370, age70Co, age70, income_deduction):
    if age1619 >= 1:
        income_deduction += 330000 * age1619
    elif age1923 >= 1:
        income_deduction += 450000 * age1923
    elif age2370 >= 1:
        income_deduction += 330000 * age2370
    elif age70Co >= 1:
        income_deduction += 450000 * age70Co
    elif age70 >= 1:
        income_deduction += 380000 * age70
    return income_deduction

def spouseDeduction_forResidentTax(selected_sp, selected_70, income_deduction, total_income):
    if selected_sp == 'nosp':
        income_deduction += 0
    elif selected_sp == 'spna' or total_income > 10000000:
        income_deduction += 0
    elif selected_sp == 'sp48':
        if selected_70 == 'spUnder70':
            if total_income <= 9000000:
                income_deduction += 330000
            elif total_income <= 9500000:
                income_deduction += 220000
            elif total_income <= 10000000:
                income_deduction += 110000
        elif selected_70 == 'sp70Plus':
            if total_income <= 9000000:
                income_deduction += 380000
            elif total_income <= 9500000:
                income_deduction += 260000
            elif total_income <= 10000000:
                income_deduction += 130000
    elif selected_sp == 'sp95' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 330000
        elif total_income <= 9500000:
            income_deduction += 220000
        elif total_income <= 10000000:
            income_deduction += 110000
    elif selected_sp == 'sp100' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 330000
        elif total_income <= 9500000:
            income_deduction += 220000
        elif total_income <= 10000000:
            income_deduction += 110000
    elif selected_sp == 'sp105' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 310000
        elif total_income <= 9500000:
            income_deduction += 210000
        elif total_income <= 10000000:
            income_deduction += 110000
    elif selected_sp == 'sp110' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 260000
        elif total_income <= 9500000:
            income_deduction += 180000
        elif total_income <= 10000000:
            income_deduction += 90000
    elif selected_sp == 'sp115' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 210000
        elif total_income <= 9500000:
            income_deduction += 140000
        elif total_income <= 10000000:
            income_deduction += 70000
    elif selected_sp == 'sp120' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 160000
        elif total_income <= 9500000:
            income_deduction += 110000
        elif total_income <= 10000000:
            income_deduction += 60000
    elif selected_sp == 'sp125' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 110000
        elif total_income <= 9500000:
            income_deduction += 80000
        elif total_income <= 10000000:
            income_deduction += 40000
    elif selected_sp == 'sp130' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 60000
        elif total_income <= 9500000:
            income_deduction += 40000
        elif total_income <= 10000000:
            income_deduction += 20000
    elif selected_sp == 'sp133' and selected_70 == 'spUnder70':
        if total_income <= 9000000:
            income_deduction += 30000
        elif total_income <= 9500000:
            income_deduction += 20000
        elif total_income <= 10000000:
            income_deduction += 10000
    return income_deduction

def studentDeduction_forResidentTax(selected_student, total_income, income_deduction):
    if selected_student == 'student' and total_income <= 750000:
        income_deduction += 260000
    elif selected_student == 'nonstudent':
        income_deduction += 0
    return income_deduction

def singleDeduction_forResidentTax(selected_single, selected_widow, total_income, income_deduction):
    if selected_single == 'single':
            if total_income <= 5000000:
                if selected_widow == 'widow': #if both single and widow applicable, apply single parent deduction
                    income_deduction += 300000
                elif not selected_widow == 'widow':
                    income_deduction += 300000
            elif total_income > 5000000:
                income_deduction += 0
    elif selected_single == 'nonsingle':
        income_deduction += 0
    return income_deduction

def widowDeduction_forResidentTax(selected_widow, selected_single, total_income, income_deduction):
    if selected_widow == 'widow': 
        if not selected_single == 'single' and total_income <= 5000000:
            income_deduction += 260000
        elif selected_widow == 'widow' and total_income > 5000000:
            income_deduction += 0
    elif selected_widow == 'nonwidow':
        income_deduction += 0
    return income_deduction

def disabilityDeduction_forResidentTax(disability, Sdisability, SdisabilityCo, income_deduction):
    if disability >= 1:
        income_deduction += 260000 * disability
    if Sdisability >= 1:
        income_deduction += 300000 * Sdisability
    if SdisabilityCo >= 1:
        income_deduction += 530000 * SdisabilityCo
    return income_deduction
        
def medicalDeduction_forResidentTax(medical, income_deduction, total_income):
    if medical >= 1 and total_income < 2000000:
        income_deduction += medical - total_income * 0.05
    elif medical <= 100000 and total_income >= 2000000:
        income_deduction += 0
    elif 100000 < medical <=2000000 and total_income >= 2000000:
        income_deduction += (medical - 100000)
    elif medical > 2100000 and total_income >= 2000000:
        income_deduction += 2000000
    return income_deduction

def lifeInsuranceDeduction_forResidentTax(lifeInsurance, nurseInsurance, pensionInsurance, income_deduction):
    if lifeInsurance > 0:
        if lifeInsurance <= 12000:
            income_deduction += lifeInsurance
        elif 12000 < lifeInsurance <= 32000:
            income_deduction += (lifeInsurance * 1/2) + 6000
        elif 32000 < lifeInsurance <= 56000:
            income_deduction += (lifeInsurance * 1/4) + 14000
        elif lifeInsurance > 56000:
            income_deduction += 40000
    if nurseInsurance > 0:
        if nurseInsurance <= 12000:
            income_deduction += nurseInsurance
        elif 12000 < nurseInsurance <= 32000:
            income_deduction += (nurseInsurance * 1/2) + 6000
        elif 32000 < nurseInsurance <= 56000:
            income_deduction += (nurseInsurance * 1/4) + 14000
        elif nurseInsurance > 56000:
            income_deduction += 28000
    if pensionInsurance > 0:
        if pensionInsurance <= 12000:
            income_deduction += pensionInsurance
        elif 15000 < pensionInsurance <= 32000:
            income_deduction += (pensionInsurance * 1/2) + 6000
        elif 40000 < pensionInsurance <= 56000:
            income_deduction += (pensionInsurance * 1/4) + 14000
        elif pensionInsurance > 56000:
            income_deduction += 28000
    return income_deduction

def socialInsuranceDeduction_forResidentTax(socialInsurance, income_deduction):
    if socialInsurance >= 1:
        income_deduction += socialInsurance
    elif socialInsurance == 0:
        income_deduction += 0
    return income_deduction

def earthquakeInsuranceDeduction_forResidentTax(earthquakeInsurance, income_deduction):
    if earthquakeInsurance >= 1:
            if earthquakeInsurance > 50000:
                income_deduction += 25000
            elif earthquakeInsurance <= 50000:
                income_deduction += (earthquakeInsurance * 1/2)
    elif earthquakeInsurance == 0:
        income_deduction += 0
    return income_deduction

def calculate_finalResidentTax(income, total_income, income_deduction, selected_sp, selected_welfare, selected_single, selected_widow, disability, Sdisability):
    if selected_welfare == 'welfare' or ((selected_single == 'single' or selected_widow == 'widow' or disability >= 1 or Sdisability >= 1) and total_income <= 1350000):
        resident_tax = 0
    elif total_income <= 450000 and selected_sp == 'nosp':
        resident_tax = 5000
    elif income <= 103000:
        resident_tax = 0
    else:
        resident_tax = ((((total_income - income_deduction) * 0.1) + 5000) // 100 ) * 100
    return resident_tax
#Calculate Resident Tax End Here


#Calculate Total Tax Amount
def calculate_total_tax(income, income_tax, resident_tax):
    if income <= 1030000:
        income_tax, resident_tax = 0, 0
    elif income > 1030000:
        total_tax = income_tax + resident_tax

    return {
        'total_tax': total_tax,
        'income_tax': income_tax,
        'resident_tax': resident_tax,
    }

if __name__ == '__main__':
    app.run(debug=True, port=5001)
