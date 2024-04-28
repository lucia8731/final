from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    total_tax, income_tax, resident_tax, income_deduction, tax_deduction = None
    if request.method == 'POST':
        income = int(request.form['income'])
        age1619 = int(request.form['age1619'])
        age1923 = int(request.form['age1923'])
        age2370 = int(request.form['age2370'])
        age70Co = int(request.form['age70'])
        age70 = int(request.form['age70s'])
        nosp_checked = request.form.get('nosp') == 'checked'
        sp48_checked = request.form.get('sp48') == 'checked'
        sp95_checked = request.form.get('sp95') == 'checked'
        sp100_checked = request.form.get('sp100') == 'checked'
        sp105_checked = request.form.get('sp105') == 'checked'
        sp110_checked = request.form.get('sp110') == 'checked'
        sp115_checked = request.form.get('sp115') == 'checked'
        sp120_checked = request.form.get('sp120') == 'checked'
        sp125_checked = request.form.get('sp125') == 'checked'
        sp130_checked = request.form.get('sp130') == 'checked'
        sp133_checked = request.form.get('sp133') == 'checked'
        spUnder70_checked = request.form.get('spUnder70') == 'checked'
        sp70Plus_checked = request.form.get('sp70Plus') == 'checked'
        student_checked = request.form.get('student') == 'checked'
        single_checked = request.form.get('single') == 'checked'
        widow_checked = request.form.get('widow') == 'checked'
        disability = int(request.form['disability'])
        Sdisability = int(request.form['Sdisability'])
        SdisabilityCo = int(request.form['SdisabilityCo'])
        welfare_checked = request.form.get('welfare') == 'checked'
        medical = int(request.form['medical'])
        lifeInsurance = int(request.form.get['life'])
        nurseInsurance = int(request.form.get['nurse'])
        pensionInsurance = int(request.form.get['pension'])
        socialInsurance = int(request.form['social'])
        earthquakeInsurance = int(request.form['earth'])

        result = calculate_tax(income)
    return render_template('index.html', total_tax=result['total_tax'], income_tax=result['income_tax'], resident_tax=result['resident_tax'], income_deduction=result['income_deduction'], tax_deduction=result['tax_deduction'])


def calculate_tax(income, age1619, age1923, age2370, age70, age70Co, nosp_checked, sp48_checked, sp95_checked, sp100_checked, sp105_checked, sp110_checked, sp115_checked, sp120_checked, sp125_checked, sp130_checked, sp133_checked, spUnder70_checked, sp70Plus_checked, student_checked, single_checked, widow_checked, disability, Sdisability, SdisabilityCo, welfare_checked, medical, lifeInsurance, nurseInsurance, pensionInsurance, socialInsurance, earthquakeInsurance):
    total_tax, income_tax, resident_tax, income_deduction = 0 #skip tax deduction for now

    #calculate total income amount
    if income <= 1625000:
        total_income = income - 550000
    elif income <= 1800000:
        total_income = (income*0.4) - 100000
    elif income <= 3600000:
        total_income = (income*0.3) + 80000
    elif income <= 6600000:
        total_income = (income*0.2) + 440000
    elif income <= 8500000:
        total_income = (income*0.1) + 1100000
    elif income >= 8500001:
        total_income = 1950000
    
    ### calculate income tax ###
    if income >= 1030001:
        #calculate taxable income
        taxable_income = 0
        income_deduction = 0

        #calculate basic deduction
        if total_income <= 2400000:
            income_deduction += 480000
        elif total_income <= 24500000:
            income_deduction += 320000
        elif total_income <= 25000000:
            income_deduction += 160000
        elif total_income >= 25000001:
            income_deduction += 0
        
        #calculate dependents deduction
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

        #calculate spouse deduction
        if nosp_checked:
            income_deduction += 0
        elif sp133_checked or total_income > 10000000:
            income_deduction += 0
        elif sp48_checked:
            if spUnder70_checked:
                if total_income <= 9000000:
                    income_deduction += 380000
                elif total_income <= 9500000:
                    income_deduction += 260000
                elif total_income <= 10000000:
                    income_deduction += 130000
            elif sp70Plus_checked:
                if total_income <= 9000000:
                    income_deduction += 480000
                elif total_income <= 9500000:
                    income_deduction += 320000
                elif total_income <= 10000000:
                    income_deduction += 160000
        elif sp95_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 380000
            elif total_income <= 9500000:
                income_deduction += 280000
            elif total_income <= 10000000:
                income_deduction += 130000
        elif sp100_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 360000
            elif total_income <= 9500000:
                income_deduction += 240000
            elif total_income <= 10000000:
                income_deduction += 120000
        elif sp105_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 310000
            elif total_income <= 9500000:
                income_deduction += 210000
            elif total_income <= 10000000:
                income_deduction += 110000
        elif sp110_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 210000
            elif total_income <= 9500000:
                income_deduction += 140000
            elif total_income <= 10000000:
                income_deduction += 70000
        elif sp115_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 210000
            elif total_income <= 9500000:
                income_deduction += 140000
            elif total_income <= 10000000:
                income_deduction += 70000
        elif sp120_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 160000
            elif total_income <= 9500000:
                income_deduction += 110000
            elif total_income <= 10000000:
                income_deduction += 60000
        elif sp125_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 110000
            elif total_income <= 9500000:
                income_deduction += 80000
            elif total_income <= 10000000:
                income_deduction += 40000
        elif sp130_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 60000
            elif total_income <= 9500000:
                income_deduction += 40000
            elif total_income <= 10000000:
                income_deduction += 20000
        elif sp133_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 30000
            elif total_income <= 9500000:
                income_deduction += 20000
            elif total_income <= 10000000:
                income_deduction += 10000
        
        #calculate working student deduction
        if student_checked and total_income <= 750000:
            income_deduction += 270000
        
        #calculate deduction for single parent
        if single_checked:
            if total_income <= 5000000:
                if widow_checked: #if both single and widow applicable, apply single parent deduction
                    income_deduction += 350000
                elif not widow_checked:
                    income_deduction += 350000
            elif total_income > 5000000:
                income_deduction += 0
        
        #calculate  deduction for widow
        if widow_checked: 
            if not single_checked and total_income <= 5000000:
                income_deduction += 270000
            elif widow_checked and total_income >= 5000001:
                income_deduction += 0
        
        #calculate deduction for people with disabilities
        if disability >= 1:
            income_deduction += 270000 * disability
        if Sdisability >= 1:
            income_deduction += 400000 * Sdisability
        if SdisabilityCo >= 1:
            income_deduction += 750000 * SdisabilityCo
        
        #calculate medical deduction
        if medical >= 1 and total_income < 2000000:
            income_deduction += medical - total_income * 0.05
        elif medical <= 100000 and total_income >= 2000000:
            income_deduction += 0
        elif 100000 < medical <=2000000 and total_income >= 2000000:
            income_deduction += (medical - 100000)
        elif medical > 2100000 and total_income >= 2000000:
            income_deduction += 2000000

        #calculate life insurance premiums deductions
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

        #calculate social insurance premiums deduction
        if socialInsurance >= 1:
            income_deduction += socialInsurance
        elif socialInsurance == 0:
            income_deduction += 0
        
        #calculate deduction for earthquake insurance premiums
        if earthquakeInsurance >= 1:
            if earthquakeInsurance > 50000:
                income_deduction += 50000
            elif earthquakeInsurance <= 50000:
                income_deduction += earthquakeInsurance
        elif earthquakeInsurance == 0:
            income_deduction += 0 
    elif income <= 1030000:
        taxable_income = 0
        income_deduction = 0
    
    #calculate tac deduction
    tax_deduction = 0 #Skip for now

    #calculate taxable income
    taxable_income = total_income - income_deduction 

    #calculate standard income tax
    if taxable_income <= 1950000:
        standard_income_tax = taxable_income * 0.05
    elif 1950000 < taxable_income <= 3300000:
        standard_income_tax = taxable_income * 0.1
    elif 3300000 < taxable_income <= 6950000:
        standard_income_tax = taxable_income * 0.2
    elif 6950000 < taxable_income <= 9000000:
        standard_income_tax = taxable_income * 0.23
    elif 9000000 < taxable_income <= 18000000:
        standard_income_tax = taxable_income * 0.33
    elif 18000000 < taxable_income <= 4000000:
        standard_income_tax = taxable_income * 0.4
    elif 40000000 < taxable_income:
        standard_income_tax = taxable_income * 0.45
    
    #calculate final income tax by adding reconstruction income tax
    income_tax += standard_income_tax - tax_deduction + (standard_income_tax * 0.021)
    ### calculating income tax END here ###
    
    ### calculate resident tax ###
    #calculate income deduction for resident tax
    income_deduction = 0
    tax_deduction = 0
    taxable_income = 0
    
    if income > 1030000:
        #calculate taxable income
        #calculate basic deduction
        if total_income <= 2400000:
            income_deduction += 430000
        elif total_income <= 24500000:
            income_deduction += 290000
        elif total_income <= 25000000:
            income_deduction += 150000
        elif total_income > 25000000:
            income_deduction += 0
        
        #calculate dependents deduction
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

        #calculate spouse deduction
        if nosp_checked:
            income_deduction += 0
        elif sp133_checked or total_income > 10000000:
            income_deduction += 0
        elif sp48_checked:
            if spUnder70_checked:
                if total_income <= 9000000:
                    income_deduction += 330000
                elif total_income <= 9500000:
                    income_deduction += 220000
                elif total_income <= 10000000:
                    income_deduction += 110000
            elif sp70Plus_checked:
                if total_income <= 9000000:
                    income_deduction += 380000
                elif total_income <= 9500000:
                    income_deduction += 260000
                elif total_income <= 10000000:
                    income_deduction += 130000
        elif sp95_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 330000
            elif total_income <= 9500000:
                income_deduction += 220000
            elif total_income <= 10000000:
                income_deduction += 110000
        elif sp100_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 330000
            elif total_income <= 9500000:
                income_deduction += 220000
            elif total_income <= 10000000:
                income_deduction += 110000
        elif sp105_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 310000
            elif total_income <= 9500000:
                income_deduction += 210000
            elif total_income <= 10000000:
                income_deduction += 110000
        elif sp110_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 260000
            elif total_income <= 9500000:
                income_deduction += 180000
            elif total_income <= 10000000:
                income_deduction += 90000
        elif sp115_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 210000
            elif total_income <= 9500000:
                income_deduction += 140000
            elif total_income <= 10000000:
                income_deduction += 70000
        elif sp120_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 160000
            elif total_income <= 9500000:
                income_deduction += 110000
            elif total_income <= 10000000:
                income_deduction += 60000
        elif sp125_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 110000
            elif total_income <= 9500000:
                income_deduction += 80000
            elif total_income <= 10000000:
                income_deduction += 40000
        elif sp130_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 60000
            elif total_income <= 9500000:
                income_deduction += 40000
            elif total_income <= 10000000:
                income_deduction += 20000
        elif sp133_checked and spUnder70_checked:
            if total_income <= 9000000:
                income_deduction += 30000
            elif total_income <= 9500000:
                income_deduction += 20000
            elif total_income <= 10000000:
                income_deduction += 10000
        
        #calculate working student deduction
        if student_checked and total_income <= 750000:
            income_deduction += 260000
        
        #calculate deduction for single parent
        if single_checked:
            if total_income <= 5000000:
                if widow_checked: #if both single and widow applicable, apply single parent deduction
                    income_deduction += 300000
                elif not widow_checked:
                    income_deduction += 300000
            elif total_income > 5000000:
                income_deduction += 0
        
        #calculate  deduction for widow
        if widow_checked: 
            if not single_checked and total_income <= 5000000:
                income_deduction += 260000
            elif widow_checked and total_income > 5000000:
                income_deduction += 0
        
        #calculate deduction for people with disabilities
        if disability >= 1:
            income_deduction += 260000 * disability
        if Sdisability >= 1:
            income_deduction += 300000 * Sdisability
        if SdisabilityCo >= 1:
            income_deduction += 530000 * SdisabilityCo
        
        #calculate medical deduction
        if medical >= 1 and total_income < 2000000:
            income_deduction += medical - total_income * 0.05
        elif medical <= 100000 and total_income >= 2000000:
            income_deduction += 0
        elif 100000 < medical <=2000000 and total_income >= 2000000:
            income_deduction += (medical - 100000)
        elif medical > 2100000 and total_income >= 2000000:
            income_deduction += 2000000

        #calculate life insurance premiums deductions
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
            if pensionInsurance <= 15000:
                income_deduction += pensionInsurance
            elif 15000 < pensionInsurance <= 40000:
                income_deduction += (pensionInsurance * 1/2) + 7500
            elif 40000 < pensionInsurance <= 70000:
                income_deduction += (pensionInsurance * 1/4) + 175000
            elif pensionInsurance > 70000:
                income_deduction += 35000

        #calculate social insurance premiums deduction
        if socialInsurance >= 1:
            income_deduction += socialInsurance
        elif socialInsurance == 0:
            income_deduction += 0
        
        #calculate deduction for earthquake insurance premiums
        if earthquakeInsurance >= 1:
            if earthquakeInsurance > 50000:
                income_deduction += 25000
            elif earthquakeInsurance <= 50000:
                income_deduction += (earthquakeInsurance * 1/2)
        elif earthquakeInsurance == 0:
            income_deduction += 0
    elif income <= 1030000:
        taxable_income = 0
        income_deduction = 0
    
    #calculate tax deduction
    tax_deduction = 0 #Skip for now

    #calculate taxable income
    taxable_income = total_income - income_deduction

    if welfare_checked or ((single_checked or widow_checked or disability or Sdisability) and total_income <= 1350000):
        resident_tax = 0
    elif total_income <= 450000 and nosp_checked:
        resident_tax = 5000
    elif income <= 103000:
        resident_tax = 0
    else:
        resident_tax = (taxable_income * 0.1) - tax_deduction + 5000
    ### calculate resident tax end here ###
            
    #calculate total tax 
    total_tax = income_tax + resident_tax

    return {
        'total_tax': total_tax,
        'income_tax': income_tax,
        'resident_tax': resident_tax,
        'income_deduction': income_deduction,
        'tax_deduction': tax_deduction
    }

if __name__ == '__main__':
    app.run(debug=True)
