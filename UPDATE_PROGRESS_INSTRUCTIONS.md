# Instructions for Updating Progress

## Purpose:
These instructions guide Copilot to dynamically update the `MASTER_GOAL_PROGRESS.md` file by scanning the project and evaluating progress.

## Steps:
1. **Perform a Full Project Scan**:
   - Scan all files in the root folder and subfolders.
   - Identify the current state of each file (e.g., completeness, alignment with the master goal).

2. **Evaluate File Progress**:
   - Assign a progress percentage to each file based on its completeness.
   - Use the following criteria:
     - **100%**: File is complete and fully aligned with the master goal.
     - **75%**: File is mostly complete but needs minor adjustments.
     - **50%**: File is partially complete and requires significant updates.
     - **25%**: File exists but is incomplete or misaligned.
     - **0%**: File is missing or irrelevant.

3. **Calculate Overall Progress**:
   - Use the average progress percentage of all files to determine the overall progress.

4. **Update `MASTER_GOAL_PROGRESS.md`**:
   - Replace the current progress percentage with the new value.
   - Update the file breakdown with the latest progress percentages.

5. **Repeat Regularly**:
   - Perform this scan and update process after every significant change to the project.

---

## Example Command for Copilot:
```text
Scan the entire project workspace, evaluate the progress of each file, and update the `MASTER_GOAL_PROGRESS.md` file with the latest progress percentage and file breakdown.
```

## Quick Prompt for Manual Trigger

Use the following prompt to manually update the `MASTER_GOAL_PROGRESS.md` file:

```text
Scan the root folder and update the `MASTER_GOAL_PROGRESS.md` file with the latest progress percentage and file breakdown.
```

Activate this prompt whenever you want to check and update the progress dynamically.
