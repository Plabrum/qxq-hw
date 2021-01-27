from qiskit.circuit.quantumcircuit import QuantumCircuit
from matplotlib.figure import Figure

def green(string):
    return ('\033[92m' + string + '\033[0m')
def red(string):
    return ('\033[91m' + string + '\033[0m')
def blue(string):
    return ('\033[96m' + string + '\033[0m')

circuit = ("circuit", QuantumCircuit)
graph = ("graph", Figure)
statvector = ("list", list)

hw16_question_list = {
    "1":[
    ("a", "qxq_q1a", circuit),
    ("b", "qxq_q1b", circuit),
    ("c", "qxq_q1c", circuit),
    ("d", "qxq_q1d", circuit),],

    "2":[
    ("a", "qxq_q2a", circuit),
    ("b", "qxq_q2b", graph),],

    "3":[
    ("a", "qxq_q3a", statvector),
    ("b", "qxq_q3b", statvector),
    ("c", "qxq_q3c", statvector),],

    "4":[
    ("a", "qxq_q4a", circuit),
    ("b", "qxq_q4b", graph),
    ("c", "qxq_q4c", circuit),
    ("d", "qxq_q4d", graph),],

    "5":[
    ("a", "qxq_q5a", circuit),
    ("b", "qxq_q5b", graph),
    ("c", "qxq_q5c", circuit),
    ("d", "qxq_q5d", graph),
    ("e", "qxq_q5e", circuit),
    ("f", "qxq_q5f", graph)]
}

def test(question_id, submitted, expected_object):
    if type(submitted) == type(None):
        print(red("It doesn't look like anything is submitted for question "+question_id
            +" make sure you've set qxq_q"+question_id+"= to your answer"))
        return False
    if type(submitted) != expected_object[1]:
        print(red("It looks like you've submitted the wrong object type for Question "+question_id+
            " we were expecting a "+expected_object[0]+" type object"))
        return False
    return True

def check(submitted_questions_dict=None):
    question_keys = hw16_question_list.keys()
    for question_num in question_keys:
        for question in hw16_question_list[question_num]:
            question_id = question_num+question[0]
            print(blue("Checking Question "+question_id+"\n"))
            if not test(question_id, submitted_questions_dict[question[1]], question[2]):
                return print(red("Keep Trying!"))
            else:
                print(green("Queston "+question_id+" Passed!\n"))
    return print(green("Everything is the right type! You're good to submit!"))


def submit(name, student_id, time_spent_hrs):
    print(green("Submitted!"))
