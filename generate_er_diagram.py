from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

with Diagram("ER Diagram for Patient Management", show=False, outformat="png", filename="ER-Diagram"):
    with Cluster("Patients"):
        patients = Custom(
            "Patients\n- patient_id (PK)\n- first_name\n- last_name\n- date_of_birth\n- gender\n- phone\n- email (Unique)\n- address",
            "./rectangle.png"
        )

    with Cluster("Insurance"):
        insurance = Custom(
            "Insurance\n- insurance_id (PK)\n- patient_id (FK)\n- provider_name\n- policy_number (Unique)\n- start_date\n- end_date\n- coverage_details",
            "./rectangle.png"
        )

    with Cluster("Appointments"):
        appointments = Custom(
            "Appointments\n- appointment_id (PK)\n- patient_id (FK)\n- appointment_date\n- doctor_name\n- status\n- notes",
            "./rectangle.png"
        )

    patients >> Edge(label="Has (1:N)") >> insurance
    patients >> Edge(label="Books (1:N)") >> appointments