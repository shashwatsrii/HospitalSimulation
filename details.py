from simpy import Resource


class Patient:
    def __init__(
        self,
        name,
        diagnosis={"diagnosis": ["Injuries", "Allergies", "Respiratory Problems","xyz","abc"]},
        prescriptions={"prescriptions": []},
        bill={
            "general practice": {
                "office visit fee": 0,
                "routine check-up fee": 0,
                "vaccination fee": 0,
                "lab test fee": 0,
            },
            "specialty care": {
                "consultation fee": 0,
                "procedure fee": 0,
                "diagnostic imaging fee": 0,
            },
            "emergency care": {
                "emergency room fee": 0, 
                "urgent care fee": 0
            },
            "hospital care": {
                "room and board fee": 0,
                "surgery fee": 0,
                "anesthesia fee": 0,
                "medication fee": 0,
            },
        },
        bill_total=0,
    ):
        self.name = name
        self.diagnosis = diagnosis
        self.prescriptions = prescriptions
        self.bill = bill
        self.bill_total = bill_total

    def __str__(self):
        return f"Patient(name={self.name}\n problem={self.diagnosis} \n prescriptions={self.prescriptions} \n bill={self.bill})"
