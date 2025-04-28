import os
from datetime import datetime

def create_meeting_notes():
    # Toplantı bilgileri
    week_number = input("Hafta numarasını girin (ör. 15): ")
    meeting_date = input("Toplantı tarihini girin (ör. April 28, 2025): ")
    attendees = input("Katılımcıları girin (ör. Selen Parlar, Team A, Team B): ")
    wbs_item = input("İlgili WBS öğesini girin (ör. 6.1): ")

    # Markdown içeriği
    meeting_notes = f"""# Weekly Project Meeting Notes - Week {week_number}

**Date:** {meeting_date}  
**Attendees:** {attendees}  
**Related WBS Item:** {wbs_item} - Conduct Weekly Project Meetings and Status Updates  

## Agenda
1. Review progress on tasks.
2. Identify problems and blockers.
3. Assign action items and record new issues if needed.

## Task Progress Review
"""

    # Görev ilerleme durumu
    num_tasks = int(input("Kaç görev durumu eklenecek? "))
    for i in range(num_tasks):
        task_name = input(f"Görev {i+1} adını girin: ")
        assigned_to = input(f"Görev {i+1} kime atandı? ")
        status = input(f"Görev {i+1} durumu (% olarak, ör. 80%): ")
        update = input(f"Görev {i+1} için güncelleme: ")
        comments = input(f"Görev {i+1} için yorumlar: ")

        meeting_notes += f"""
- **Task {i+1}: {task_name} (Assigned to {assigned_to})**  
  - **Status:** {status} complete.  
  - **Update:** {update}  
  - **Comments:** {comments}
"""

    # Sorunlar
    meeting_notes += "\n## Problems Identified\n"
    num_problems = int(input("Kaç sorun tanımlandı? "))
    for i in range(num_problems):
        problem_desc = input(f"Sorun {i+1} açıklaması: ")
        impact = input(f"Sorun {i+1} etkisi: ")
        discussion = input(f"Sorun {i+1} için tartışma: ")

        meeting_notes += f"""
{i+1}. **{problem_desc}**  
   - **Description:** {problem_desc}  
   - **Impact:** {impact}  
   - **Discussion:** {discussion}  
"""

    # Aksiyon öğeleri
    meeting_notes += "\n## Action Items\n"
    num_actions = int(input("Kaç aksiyon öğesi eklenecek? "))
    for i in range(num_actions):
        issue_number = input(f"Aksiyon öğesi {i+1} için issue numarası (ör. 16): ")
        assignee = input(f"Aksiyon öğesi {i+1} kime atandı? ")
        description = input(f"Aksiyon öğesi {i+1} açıklaması: ")
        priority = input(f"Aksiyon öğesi {i+1} önceliği (High/Medium/Low): ")
        status = input(f"Aksiyon öğesi {i+1} durumu (ör. To be created): ")

        meeting_notes += f"""
{i+1}. **New Issue #{issue_number}: {description}**  
   - **Assignee:** {assignee}  
   - **Description:** {description}  
   - **Priority:** {priority}  
   - **Status:** {status}  
"""

    # Sonraki adımlar
    next_steps = input("Sonraki adımları girin: ")
    meeting_notes += f"""
## Next Steps
- {next_steps}

**Location for Notes:** `/docs/meeting-notes/week-{week_number}.md`

**Meeting Adjourned:** {datetime.now().strftime('%I:%M %p')}
"""

    # Dosyayı kaydet
    output_dir = "docs/meeting-notes"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"week-{week_number}.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(meeting_notes)

    print(f"Toplantı notları başarıyla '{file_path}' dosyasına kaydedildi.")

if __name__ == "__main__":
    create_meeting_notes()
