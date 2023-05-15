import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import details as details
import processes as processes


class HospitalSimulator:
    def __init__(self, patient: details.Patient):
        self.patient = patient

        self.root = tk.Tk()
        self.root.configure(bg="white")
        self.root.geometry("500x500")
        self.choice = "None"
        self.root.title("Hospital")
        self.title_label = tk.Label(
            self.root,
            text="Hospital Simulation",
            font=("Times New Roman", 30),
            bg="white",
        )
        self.title_label.grid(row=1, column=1,padx=80)

        self.patientWindow = tk.Label(
            self.root, text=f"Patient Window", font=("Times New Roman", 15), bg="white"
        )
        self.patientWindow.grid(row=2, column=1)

        # Now, we have 4 options to choose from, regarding the patient's problem.
        self.image = Image.open("doctor.png")
        self.image = self.image.resize((300, 300))
        self.doctorImage = ImageTk.PhotoImage(self.image)
        self.Labelimg = tk.Label(self.root, image=self.doctorImage).grid(
            row=4, column=1,
        )
        self.doctorLabel = tk.Label(self.root, text="Doctor Here")
        self.doctorLabel.grid(row=3, column=1)
        self.doctorButton = tk.Button(
            self.root,
            text="Meet the Doctor",
            command=lambda: self.run("meetDoctor"),
            bg="Black",
            fg="white",
            font=("Times New Roman", 10),
        )
        self.doctorButton.grid(row=6, column=1)

    def run(self, meetDoctor):
        choice = meetDoctor
        if choice != "None":
            if choice == "meetDoctor":
                processes.DoctorFunction(patient=self.patient)
            else:
                print("You could not meet the doctor")
                
if __name__ == "__main__":
    patient = details.Patient(
        name="Shashwat"
    )
    simulator = HospitalSimulator(patient=patient)

    simulator.root.mainloop()
