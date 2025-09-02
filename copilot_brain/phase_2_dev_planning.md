

# Phase 2 – Planning How Your App Will Work (For Everyone)

**Note:** For a full list and explanation of software development methods (like Agile or Scrum), see [`copilot_brain/methodologies_and_best_practices.md`](methodologies_and_best_practices.md).

---

## How This Step Works

**What Copilot will do automatically:**
- Copilot can create all the main planning documents for you, based on your answers from Phase 1.
- Copilot can also generate diagrams and technical details if you don’t have them.

**What you need to do:**
- If you have your own diagrams or ideas for how the app should work, you can upload or describe them when asked.
- If not, just say “continue” and Copilot will do the rest.

**Tip:** Copilot will always ask before overwriting anything you’ve provided.

---

## What You’ll Create in This Step
You’ll end up with these files (Copilot will save them in the right place):
- screen_flows/[flow_name].mmd
- deliverables/[screen_name]/*.md
- system_architecture.md
- integration_view.md
- functional_architecture.md
- component_architecture.md
- acceptance_criteria.md
- tech_stack.md

This phase is about planning how your app will work, what screens it will have, and what technology will be used. You don’t need to know any technical terms—just answer questions in your own words, or let Copilot do it for you.

---

---

### Step 1 – Finalize Screen Flows

At this step, the user can proceed in one of two ways:

**Option A – Upload Finalized Screen Flows**  
⚠️ Reminder: If you choose Option A, you must ensure that you upload **all screen flows for your entire app**. Missing screens will cause problems later in Phase 2 and Phase 3.  

**Step 1A:** The agent will ask the user to upload all screen flows into:  
`phase2/development_planning/screen_flows/`  

**Step 2A:** The agent will ask:  
*“Are these ALL of the screen flows for your app? If any screens are missing, you will have problems later.”*  

- If **Yes** → proceed to Step 4A.  
- If **No** → proceed to Step 3A.  

**Step 3A:** The agent will ask the user to upload the **Phase 1 summary**.  
- The agent analyzes the Phase 1 outputs, compares them against the uploaded screen flows, and determines the **remaining screens that must be generated**.  
- The agent provides a brief description of each missing screen and asks if the user would like to proceed to Step 3B.  

**Step 3B:** The agent generates the missing screens one at a time:  
1. Screen Title  
2. Brief Description  
3. Mermaid Diagram Code (inside a code block, for easy copy/paste and visual check)  

After each generation, the agent shows progress:  
*“Screen [X] of [Total] generated ✅ (next up: [Next Screen Title])”*  

The agent then asks the user:  
*“Would you like me to generate the next screen?”*  

**Step 3C:** When all missing screens are generated, the agent confirms:  
*“All [Total] screens have been generated. Step 1 of Phase 2 is complete ✅. Would you like to move on to Step 2 (Split Flows Into Deliverables)?”*  

**Step 4A:** If the user confirmed that all screens were uploaded in Step 2A, the agent will confirm:  
*“All [Total] screens have been uploaded. Step 1 of Phase 2 is complete ✅. Would you like to move on to Step 2 (Split Flows Into Deliverables)?”*
  

**Option B – Generate Screen Flows from Phase 1 Outputs**  
If the user does not have finalized flows, the agent will generate them based on the Phase 1 Concept & Strategy summary.  
This process is broken into three sub-steps:

1. **Analyze Phase 1 Summary**  
   - The agent analyzes the Phase 1 outputs and determines the full set of required screens.  
   - The agent provides:  
     - A numbered list of all screens to be generated.  
     - A brief description of each screen.  
     - The total number of screens.  
   - The agent then asks:  
     *“Would you like to begin generating these screen flows now?”*

2. **Generate Screen Flows One at a Time**  
   - For each screen, the agent generates:  
     1. Screen Title  
     2. Brief Description  
     3. Mermaid Diagram Code (in a code block, for easy copy/paste and visual check)  
   - After each screen, the agent shows progress:  
     *“Screen [X] of [Total] generated ✅ (next up: [Next Screen Title])”*  
   - The agent asks the user:  
     *“Would you like me to generate the next screen?”*  

3. **Complete Step 1**  
   - When all screens are generated, the agent confirms:  
     *“All [Total] screens have been generated. Step 1 of Phase 2 is complete ✅. Would you like to move on to Step 2 (Split Flows Into Deliverables)?”*


---

## Step 2 – Split Flows Into Deliverables
Upload one of your detailed screen flow diagrams. I will take that diagram and generate six deliverables from it, one at a time:  

1. User Flow – step-by-step interactions  
2. Data Flow – how data moves through the system  
3. State Management Flow – loading, success, error states  
4. API/Service Flow – calls, responses, retries  
5. Error/Exception Flow – timeouts, disconnections, retries  
6. Security/Privacy Flow – permissions, safe handling  

Each deliverable will be provided in three formats: a plain English explanation, a Mermaid code version (so you can visualize it in Mermaid), and a downloadable file containing that Mermaid code.  

Once you have all six deliverables for a screen, download them and place them into the Deliverables folder inside Phase 2 – Development Planning. Within that folder, create a subfolder named after the screen, using lowercase letters with underscores (for example, call_screen). Place the six deliverables for that screen inside its subfolder.  

Repeat this process for each of your screen flow diagrams until every flow has been broken down.

Naming Note:
For Mermaid diagrams, always use lowercase_with_underscores for node IDs (e.g., call_screen, retry_button).
Labels may use natural names with spaces (e.g., “Call Screen”, “Retry Button”). This ensures your diagrams remain valid while staying user-friendly.

---

## Step 3 – System Architecture

**First Generation**  
Start by answering this question:  
**“How many high-detail screen flows did you complete in Step 2?”**  

This is important because it allows me to track how many batches of six deliverables you will be uploading in this step.

---

**Second Generation (after you answer)**  
Here’s what to do next:  

1. For each screen flow, upload the six deliverables you generated in Step 2 (user flow, data flow, state flow, API/service flow, error/exception flow, security/privacy flow).  
2. Upload one full batch of six at a time. After each batch, I will:  
   - Confirm and keep track of progress (for example: *2 of 5 screen flows uploaded*).  
   - Generate a **compact summary** of the batch (capturing only the key requirements and design implications). This summary will remain in memory to represent the screen in later steps, so we don’t exceed context limits.  
   - You should save the full six deliverables for each screen into your project folder (`phase2/development_planning/deliverables/[screen_name]/`).  
3. Once all batches have been uploaded, I will use the collected summaries to perform a deep web search and gather the most up-to-date guidance on system architecture.  
4. I will recommend a **System Architecture** covering frontend, backend, media/calling layer, and data storage, based on both your flows and the latest best practices.  
5. I will present the recommendation to you and ask: *Do you want to use this system architecture?*  
   - If **Yes** → we lock it in and proceed to Step 4. I will also create a **downloadable markdown file** containing the chosen system architecture. Save this file into your project folder under `phase2/development_planning/system_architecture.md`.  
   - If **No** → I will repeat the deep web search and present an alternative, until you are satisfied.    

Reminder on Naming:
Please make sure all your flows follow this convention:

Node IDs → lowercase_with_underscores

Labels → natural names with spaces

This approach ensures that all of your flows are considered together, while still keeping the process manageable by summarizing each batch. You keep the full deliverables safe in your folder, while I rely on summaries to design the architecture.

---

## Step 4 – Flow Integration

Now that your system architecture is chosen, the next step is to integrate your flows at the system level.  

Here’s what to do:  
1. Upload your finalized user flows from Step 2 and the System_Architecture.md file from Step 3.  
2. I will map each user flow against the backend services they depend on.  
3. I will make sure error-handling paths are represented (timeouts, retries, declined calls).  
4. I will cross-check the flows against the contract definitions (from your interface and error code docs) to confirm accuracy.  

When I finish, I will generate a clear, downloadable markdown file that shows how your flows interact with backend services and error paths at the system level.  

👉 Save this file into your project folder under:  
`phase2/development_planning/integration_view.md`  

This Integration View will then be used in Step 5 to map flows to functionality.

---

## Step 5 – Functional Architecture

Now that your flows are integrated, it’s time to link them directly to system functionality.  

Here’s what to do:  
1. Upload the Integration_View.md file generated in Step 4.  
2. I will map each screen flow to the system functions it supports (for example: login flow → authentication service, call flow → signaling + scoring service).  
3. I will highlight dependencies between features so you can see what must be in place for each function to work correctly.  

When I finish, I will create a clear, downloadable markdown file that shows how each screen flow connects to system functions and their dependencies.  

👉 Save this file into your project folder under:  
`phase2/development_planning/functional_architecture.md`  

This Functional Architecture file will then be used in Step 6 to break the system down into components.


---

## Step 6 – Component Architecture

Now that you have a Functional Architecture, the next step is to break it down into concrete components.  

Here’s what to do:  
1. Upload the Functional_Architecture.md file generated in Step 5.  
2. I will use it to define the main building blocks of your system, including:  
   - UI components (screens, forms, navigation pieces)  
   - Backend services (APIs, data handlers, signaling services)  
   - Helper modules (utilities, error handlers, shared logic)  
3. For each component, I will make sure it:  
   - Has clear contracts (interfaces, events, and error handling rules)  
   - Includes observability hooks (logs, metrics, alerts)  
   - Follows coding standards (linting, formatting, pre-commit rules)  
   - Is compatible with your developer environment (`.devcontainer`, `.vscode`)  

When I finish, I will create a clear, downloadable markdown file that lists every component and its responsibilities.  

👉 Save this file into your project folder under:  
`phase2/development_planning/component_architecture.md`  

This Component Architecture file will then be used in Step 7 to define acceptance criteria for each part of the system.

---

## Step 7 – Acceptance Criteria

With your Component Architecture in place, the next step is to define clear success conditions for each component and flow.  

Here’s what to do:  
1. Upload the Component_Architecture.md file generated in Step 6.  
2. I will generate measurable acceptance criteria for every major feature and component. These criteria will include performance, reliability, security, and testability requirements.  
3. Examples of criteria I will include:  
   - Calls must connect within 3 seconds under load.  
   - Retry logic activates correctly on timeout.  
   - No secrets or sensitive data are hardcoded.  
   - Golden path flows always succeed.  
   - Regression tests pass for previously working features.  
   - Recovery scenarios restore service within defined time.  
   - Observability: metrics are exposed and alerts are configured.  
   - Security: code passes static analysis and secret scans.  

When I finish, I will create a clear, downloadable markdown file listing the acceptance criteria for your system.  

👉 Save this file into your project folder under:  
`phase2/development_planning/acceptance_criteria.md`  

This Acceptance Criteria file will then be used in Step 8 to help evaluate which tech stack best supports these requirements.

---

## Step 8 – Tech Stack Selection

With your acceptance criteria defined, the next step is to choose the tools and technologies that will power your app.  

Here’s what to do:  
1. Upload the Acceptance_Criteria.md file generated in Step 7.  
2. I will perform a deep web search to gather the most current (2025) best practices for frontend, backend, media/calling, and infrastructure technologies.  
3. Based on your acceptance criteria and component architecture, I will recommend a tech stack that:  
   - Supports the components you need.  
   - Works smoothly with CI/CD workflows (lint, test, build, deploy).  
   - Uses environment-aware configurations.  
   - Balances performance with infrastructure cost.  
4. If TypeScript is part of the stack, I will enforce strict configs (`tsconfig.base.json`).  
5. If a monorepo is chosen, I will recommend workspace management principles that work across npm, yarn, or pnpm.  

When I finish, I will create a clear, downloadable markdown file describing the chosen tech stack and explaining why each technology was selected.  

👉 Save this file into your project folder under:  
`phase2/development_planning/tech_stack.md`  

This Tech Stack file will complete the setup for Phase 2 and prepare you to move into Phase 3 – AI Execution.

---

## Step 9 – Deliverables of Phase 2

By the end of Phase 2, you should have a complete set of planning documents that will guide Phase 3 – AI Execution.  

Here’s what you should now have in your project folder:  
1. Finalized high-detail flow diagrams for each screen (stored in `phase2/development_planning/screen_flows/`).  
2. Six deliverables per flow (user, data, state, API, error, security), saved inside `phase2/development_planning/deliverables/[screen_name]/`.  
3. System Architecture file: `phase2/development_planning/system_architecture.md`  
4. Integration View file: `phase2/development_planning/integration_view.md`  
5. Functional Architecture file: `phase2/development_planning/functional_architecture.md`  
6. Component Architecture file: `phase2/development_planning/component_architecture.md`  
7. Acceptance Criteria file: `phase2/development_planning/acceptance_criteria.md`  
8. Tech Stack file: `phase2/development_planning/tech_stack.md`  

Confirm that each of these files is present and correctly placed in your project folder structure.  
Once everything is in place, you are ready to move into Phase 3 – AI Execution.

---

🎉 Congratulations — you’ve completed Phase 2: Development Planning!  

Here’s what you’ve accomplished across the four pillars of development:

1. **System Architecture** → [summary auto-pulled from `system_architecture.md`]  
2. **Functional Architecture** → [summary auto-pulled from `functional_architecture.md`]  
3. **Component Architecture** → [summary auto-pulled from `component_architecture.md`]  
4. **Tech Stack** → [summary auto-pulled from `tech_stack.md`]  

This gives you a complete, dynamic blueprint for moving into **Phase 3 – AI Execution**.  

Would you like to:  
1. Proceed immediately to Phase 3  
2. Take a break and return later

