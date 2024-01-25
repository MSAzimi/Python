class Patient:

    def __init__(self, id, name, family_name, age, height, weight):
        self.id = id
        self.name = name
        self.family_name = family_name
        self.age = age
        self.height = height
        self.weight = weight


class Appointment:
    def __init__(self):
        self.schedule = {}
        self.patients = []

    def add_patient(self, patient):
        if self.get_patient_by_id(patient.id) is not None:
            return "error: this ID already exists"
        if int(patient.age) < 0:
            return "error: invalid age"
        if int(patient.height) < 0:
            return "error: invalid height"
        if int(patient.weight) < 0:
            return "error: invalid weight"

        self.patients.append(patient)
        return "patient added successfully"

    def get_patient_by_id(self, id):
        for i in range(0, len(self.patients)):
            if self.patients[i].id == id:
                return self.patients[i]
        return None

    def display_patient(self, id):
        patient = self.get_patient_by_id(id)
        if patient is None:
            return "error: invalid ID"

        return f"patient name: {patient.name}\npatient family name: {patient.family_name}\npatient age: {patient.age}\npatient height: {patient.height}\npatient weight: {patient.weight}"


    def add_visit(self, id, time):
        if self.get_patient_by_id(id) is None:
            return "error: invalid id"
        if time < 9 or time > 18:
            return "error: invalid time"
        for reserve in self.schedule.keys():
            if reserve == time:
                return "error: busy time"


        self.schedule[time] = self.get_patient_by_id(id)
        return "visit added successfully!"

    def delete_patient(self, id):
        if self.get_patient_by_id(id) is None:
            return "error: invalid id"

        self.patients = [patient for patient in self.patients if patient.id != id]

        for time, patient in list(self.schedule.items()):
            if patient.id == id:
                del self.schedule[time]

        return "patient deleted successfully!"

    def display_visit_list(self):
        output = "SCHEDULE:"
        for time, patient in self.schedule.items():
            output += f"\n{time}:00 {patient.name} {patient.family_name}"
        return output
    def exit(self):
        print('\n')

#patients_list = []
#appointments_list = []
appointments = Appointment()

while True:
    command = input().strip()
    if command:
        parts = command.split()

        if parts[0] == "add" and parts[1] == "patient":
            id = int(parts[2])
            name = parts[3]
            family_name = parts[4]
            age = int(parts[5])
            height = int(parts[6])
            weight = int(parts[7])
            patient = Patient(parts[2], parts[3], parts[4], parts[5], parts[6], parts[7])
            print(appointments.add_patient(patient))
        elif parts[0] == "display" and parts[1] == "patient":
            id = int(parts[2])
            patient_displayed = appointments.display_patient(parts[2])
            print(patient_displayed)
        elif parts[0] == "add" and parts[1] == "visit":
            patient_id = int(parts[2])
            time = int(parts[3])
            patient_visited = appointments.add_visit(parts[2], int(parts[3]))
            print(patient_visited)
        elif parts[0] == "delete" and parts[1] == "patient":
            id = int(parts[2])
            Deleted = appointments.delete_patient(parts[2])
            print(Deleted)
        elif parts[0] == "display" and parts[1] == "visit" and parts[2] == "list":
            print(appointments.display_visit_list())

        elif parts[0] == "exit":
            break
        else:
            print("invalid command")
    else:
        print("invalid command")