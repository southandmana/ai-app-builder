





# How to Use the Copilot Agent System

**Collaboration & Teams:** For tips on working with others and scaling to large teams, see [`../templates_examples/roles_and_collaboration_guidance.md`](../templates_examples/roles_and_collaboration_guidance.md).

**Security & Privacy:** For a checklist and best practices to protect user data, see [`../templates_examples/security_privacy_guidance.md`](../templates_examples/security_privacy_guidance.md).

**Localization:** For tips on making your project accessible to users worldwide, see [`../templates_examples/localization_guidance.md`](../templates_examples/localization_guidance.md).

**Welcome & FAQ:** For a friendly introduction and common questions, see [`welcome_and_faq.md`](welcome_and_faq.md).

**Accessibility:** For tips and a checklist to ensure your project is inclusive, see [`../templates_examples/accessibility_guidance.md`](../templates_examples/accessibility_guidance.md).

**Note:** For a full list and explanation of software development methodologies (Agile, Scrum, Kanban, Waterfall, Lean, DevOps, etc.), see [`../copilot_brain/methodologies_and_best_practices.md`](../copilot_brain/methodologies_and_best_practices.md). This resource helps you choose the best workflow for your project and understand how industry standards apply to your process.

This guide explains how you (the user) can interact with the **Copilot Agent** system.  
It is written in plain English and avoids technical jargon where possible.

---

## 1. Purpose
The Copilot Agent allows you to **build, plan, and launch apps step-by-step** without needing coding expertise.  
It follows structured phases (Concept → Planning → Execution → Testing → Launch), while automatically managing files in the correct folders.

---

## 2. Getting Started
1. Make sure you have the `app_project/` folder with the correct structure.  
2. Check the `copilot_brain/` folder: it contains the system instructions and phase guides Copilot follows.  
3. When using Copilot, **point it to `FOLDER_STRUCTURE.md`** so it knows where to generate files.

---

## 3. How to Work with Copilot
- **Ask by Phase and Step**  
  Example:  
  > "Let’s start Phase 2 Step 2 — generate the screen flow diagrams and place them correctly."

- **Copilot Generates Automatically**  
  Copilot will create the necessary files and put them in the right subfolders.  
  Example:  
  > Creates `/phase2_development_planning/screen_flows/home_screen.mmd`.

- **Check Recall Summaries**  
  After each step, Copilot updates `/recall/phaseX_stepY_summary.md`.  
  This lets you see progress and ensures memory is never lost.

---

## 4. Folder Overview
- `copilot_brain/` → Copilot’s rules and reference materials.  
- `user_guide/` → Guides for you (this file).  
- `project_overview/` → General project notes and progress tracker.  
- `phase1–phase5/` → Actual app deliverables.  
- `recall/` → Step-by-step memory summaries.  

---

## 5. Tips for Using Copilot Effectively
- Always **confirm file paths** when Copilot generates deliverables.  
- If a file already exists, Copilot should ask before overwriting.  
- Use **lowercase_with_underscores** for naming screens and files.  
- If you change the folder structure, update `FOLDER_STRUCTURE.md` immediately.  

---

## 6. Example Workflow
1. Tell Copilot:  
   > "Start Phase 1 Step 1: define mission."  
2. Copilot generates `mission.md` inside `/phase1_concept_strategy/`.  
3. Copilot saves a summary to `/recall/phase1_step1_summary.md`.  
4. You review, then move on to the next step.

---

## 7. Support & Expansion
- If you add new features or phases, extend `FOLDER_STRUCTURE.md` so Copilot can adapt.  
- For advanced use, sub-agents (specialist coders) may be added later.  
- This system grows with your projects.

---

**In short:** You give instructions by phase/step → Copilot generates deliverables → Everything is tracked and organized.  
