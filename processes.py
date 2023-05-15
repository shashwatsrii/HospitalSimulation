# Processes
# All the processes used in the simulation are defined here.

import tkinter as tk
import simpy, simpy.rt
import details as details


def DoctorFunction(patient: details.Patient) -> None:
    # Tkinter GUI
    main = tk.Tk()
    main.title("Diagnosis")
    main.geometry("1000x600")

    header = tk.Label(
        main, text=f"Diagnosis Window", font=(2)
    )
    header.grid(row=0, column=1, pady=10, padx=10)

    textLabel = tk.Text(main)
    textLabel.grid(row=3, column=2, pady=10)

    start_button = tk.Button(
        main, text="Start Diagnosis", command=lambda: diagnosisFunction(patient), fg="black",
    )
    start_button.grid(row=2, column=1)

    thankYouText = tk.Label(main, text="",font=("Times New Roman", 10))
    thankYouText.grid(row=4, column=2)
    exit_button = tk.Button(
            main,
            text="Exit Hospital",
            command=main.destroy,            
            font=("Times New Roman", 10),
        )
    exit_button.grid(row=6, column=1)

    def diagnosisFunction(patient) -> None:
        def start_simulation(
            env: simpy.rt.RealtimeEnvironment, patient: details.Patient
        ) -> None:
            start_button.config(state=tk.DISABLED)


            textLabel.insert(tk.END, f"Doctor started the diagnosis.\n")
            main.update()
            yield env.timeout(1)

            problems = patient.diagnosis["diagnosis"]
            textLabel.insert(
                tk.END, f"Doctor found the following issues\n"
            )
            main.update()
            textLabel.insert(
                tk.END, f"1. {problems[0]}\n"
            )
            main.update()
            textLabel.insert(
                tk.END, f"2. {problems[1]}\n"
            )
            main.update()
            textLabel.insert(
                tk.END, f"3. {problems[2]}\n"
            )
            main.update()

            textLabel.insert(tk.END, "Starting the diagnosis\n")
            main.update()
            yield env.timeout(1)

            if problems.count("Injuries"):
                textLabel.insert(tk.END, "Evaluating the injuries.\n")
                main.update()

                textLabel.insert(tk.END, "Immobilizing the injured areas.\n")
                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Performing Medications.\n")                
                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Trying Physical Therapy.\n")

                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Evaluating if surgery is needed.\n")

                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Follow-up Care.\n")

                main.update()

                patient.prescriptions["prescriptions"].append("Bayer")
                patient.prescriptions["prescriptions"].append("Bufferin")
                patient.bill["general practice"]["office visit fee"] += 2500
                patient.bill["general practice"]["lab test fee"] += 220
                patient.bill_total += 2720

            if problems.count("Allergies"):
                textLabel.insert(tk.END, "Treating \n")
                main.update()

                textLabel.insert(tk.END, "~Injecting vaccines\n")
                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Medication\n")
                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Treatment for allergies successful.\n")
                main.update()

                patient.prescriptions["prescriptions"].append("Fexafenodine.")
                patient.prescriptions["prescriptions"].append("Nasal Sprays.")
                patient.bill["general practice"]["routine check-up fee"] += 1000
                patient.bill["hospital care"]["medication fee"] += 1070
                patient.bill_total += 2070

            # If problem def exists
            if problems.count("Respiratory Problems"):
                textLabel.insert(tk.END, "Evaluating the patient.\n")

                main.update()

                textLabel.insert(tk.END, "Taking Medications\n")
                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Oxygen Therapy\n")
                main.update()
                yield env.timeout(1)

                textLabel.insert(tk.END, "Applying fluids and recommended rest.\n")
                main.update()

                patient.prescriptions["prescriptions"].append("")
                patient.bill["emergency care"]["emergency room fee"] += 750
                patient.bill["emergency care"]["urgent care fee"] += 30
                patient.bill_total += 1030

            textLabel.insert(tk.END, "Prescribing medication...\n")
            main.update()
            yield env.timeout(1)
            textLabel.insert(
                tk.END, f"Prescribed: {patient.prescriptions['prescriptions']}\n"
            )
            textLabel.see(tk.END)
            main.update()

            patient.bill["specialty care"]["consultation fee"] += 670
            patient.bill_total += 670

            textLabel.insert(tk.END, f"Payment due: {patient.bill_total}\n")
            textLabel.see(tk.END)
            
            thankYouText.config(text="Thank you for visiting!")
            main.update()

        
        doctor = simpy.rt.RealtimeEnvironment(factor=1, initial_time=0)
        Hospital = doctor.process(start_simulation(doctor, patient))
        doctor.run(until=Hospital)