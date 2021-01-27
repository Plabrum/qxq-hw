def green(string):
    return ('\033[92m' + string + '\033[0m')
def red(string):
    return ('\033[91m' + string + '\033[0m')
def blue(string):
    return ('\033[96m' + string + '\033[0m')

def checker(test, string):
    if test:
        print(string)
        return True
    return False
    
def check():
    print("Checking Question 1 \n")
    
    q1_err_1 = red("Nothing Submitted for Question 1, make sure it's in the form: \n \nqxq.q1 = (your answer here)")
    q1_err_2 = red("Question 1 must be a type of QuantumCircuit()")
    if checker(type(qxq_q1) == None, q1_err_1): return print(blue("\nKeep Trying!"))
    if checker(type(qxq_q1) != q.qiskit.circuit.quantumcircuit.QuantumCircuit, q1_err_2): return print(blue("\nKeep Trying!"))
    
    print(green("Question 1 Passed! \n"))
    
    print("Checking Question 2 \n")
    
    q2_err_1 = "Nothing Submitted for Question 2, make sure it's in the form: \nqxq.q2=(your answer here)"
    q2_err_2 = "Question 2 must be a type list"
    if checker(type(qxq_q2) == None, q2_err_1): return print("\nKeep Trying!")
    if checker(type(qxq_q2) != list, q2_err_2): return print("\nKeep Trying!")
    
    print(green("Question 2 Passed! \n"))
    
    print("Checking Question 3 \n")
    
    q3_err_1 = "Nothing Submitted for Question 3, make sure it's in the form: \nqxq.q3=(your answer here)"
    q3_err_2 = "Question 3 must be a type QuantumCircuit()"
    if checker(type(qxq_q3) == None, q3_err_1): return print("\nKeep Trying!")
    if checker(type(qxq_q3) != q.qiskit.circuit.quantumcircuit.QuantumCircuit, q3_err_2): return print("\nKeep Trying!")
    
    print(green("Question 3 Passed! \n"))
    
    print("Checking Question 4 \n")
    
    q4_err_1 = "Nothing Submitted for Question 4, make sure it's in the form: \nqxq.q4=(your answer here)"
    q4_err_2 = "Question 4 must be a type plot"
    if checker(type(qxq_q4) == None, q4_err_1): return print("\nKeep Trying!")
    if checker(type(qxq_q4) != plt.matplotlib.figure.Figure, q4_err_2): return print("\nKeep Trying!")
    
    print(green("Question 4 Passed! \n"))

def submit():
    print("Submitted!")