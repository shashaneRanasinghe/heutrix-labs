import os

components = {}

components['Problem.jsx'] = """import React, { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

export default function Problem() {
  const issues = [
    "patient enquiries or referral requests are followed up differently by different people",
    "referrals, reports, recalls or document requests are hard to track end to end",
    "routine admin steps depend on memory, inbox searches or one person’s local spreadsheet",
    "reception, clinicians and practice managers do not always have the same view of what is waiting",
    "handovers between team members are inconsistent or hard to review",
    "recalls, reminders or follow-up actions are not easy to monitor",
    "the same information is copied between systems",
    "managers cannot easily see workload, bottlenecks or work in progress",
    "reporting takes too long or depends on one person",
    "AI tools are being used informally without practice-approved rules"
  ];

  const targetRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: targetRef,
  });

  const x = useTransform(scrollYProgress, [0, 1], ["0%", "-85%"]);

  return (
    <section ref={targetRef} className="h-[400vh] bg-primary relative" id="problem">
      <div className="sticky top-0 flex h-screen items-center overflow-hidden">
        
        <div className="px-lg absolute top-[10%] w-full max-w-container-max mx-auto left-0 right-0 z-10 pointer-events-none">
          <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl">
            <h2 className="font-display-md text-display-md-mobile md:text-display-md text-white mb-md drop-shadow-lg">When important work is spread across memory, inboxes and spreadsheets, even capable teams can lose visibility.</h2>
            <p className="font-body-lg text-body-lg text-on-primary-fixed-variant drop-shadow-md">
              Many practice teams are highly capable, but the systems around them have not always kept up with growth, staff changes, patient demand or disconnected tools. Heutrix Labs helps identify where important admin and operational work needs clearer ownership, tracking, reminders, handover or review.
            </p>
          </motion.div>
        </div>

        <motion.div style={{ x }} className="flex gap-lg px-lg mt-[20vh] items-center">
          <div className="w-[10vw] shrink-0" />
          
          <div className="w-[300px] shrink-0">
             <h3 className="font-display-sm text-display-sm text-secondary-fixed">You may notice:</h3>
          </div>

          {issues.map((issue, i) => (
            <motion.div 
              key={i} 
              className="w-[300px] md:w-[400px] h-[300px] bg-white rounded-xxl p-xl shadow-2xl shrink-0 flex flex-col justify-center border border-slate-200"
              whileHover={{ scale: 1.05, y: -10 }}
              transition={{ type: "spring", stiffness: 300, damping: 20 }}
            >
              <div className="w-12 h-12 rounded-full bg-error-container text-error flex items-center justify-center mb-lg">
                <span className="material-symbols-outlined text-[24px]">priority_high</span>
              </div>
              <p className="font-headline-sm text-headline-sm text-primary leading-tight">{issue}</p>
            </motion.div>
          ))}
          
          <div className="w-[400px] shrink-0 p-xl">
             <p className="font-body-lg text-body-lg text-white font-medium border-l-4 border-secondary pl-lg">
                Heutrix Labs helps turn these pressure points into clearer workflows, practical tracking systems, safer AI practices and better visibility for day-to-day decisions.
              </p>
          </div>
          
          <div className="w-[30vw] shrink-0" />
        </motion.div>

      </div>
    </section>
  );
}
"""

components['Methodology.jsx'] = """import React, { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

const HighlightText = ({ text }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start 80%", "end 40%"]
  });

  const color = useTransform(scrollYProgress, [0, 1], ["rgba(15, 23, 42, 0.2)", "rgba(15, 23, 42, 1)"]);

  return (
    <motion.span ref={ref} style={{ color }} className="transition-colors duration-100 block mb-lg">
      {text}
    </motion.span>
  );
};

const StickySection = ({ title, children, bgColor = "bg-surface" }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start start", "end end"]
  });

  const titleOpacity = useTransform(scrollYProgress, [0, 0.2, 0.8, 1], [0, 1, 1, 0]);
  const titleY = useTransform(scrollYProgress, [0, 0.2, 0.8, 1], [50, 0, 0, -50]);
  
  const contentOpacity = useTransform(scrollYProgress, [0.3, 0.5, 0.8, 1], [0, 1, 1, 0]);
  const contentY = useTransform(scrollYProgress, [0.3, 0.5, 0.8, 1], [100, 0, 0, -100]);
  const contentFilter = useTransform(scrollYProgress, [0.3, 0.5], ["blur(10px)", "blur(0px)"]);

  const titleColor = bgColor === "bg-primary" ? "text-white" : "text-primary";

  return (
    <section ref={ref} className={`h-[250vh] ${bgColor} relative z-20`}>
      <div className="sticky top-0 h-screen flex flex-col md:flex-row items-center justify-center px-lg gap-xl max-w-container-max mx-auto overflow-hidden">
        <motion.div style={{ opacity: titleOpacity, y: titleY }} className="flex-1">
          <h2 className={`font-display-md text-display-md-mobile md:text-display-md ${titleColor}`}>{title}</h2>
        </motion.div>
        <motion.div style={{ opacity: contentOpacity, y: contentY, filter: contentFilter }} className="flex-1">
          {children}
        </motion.div>
      </div>
    </section>
  );
};

export default function Methodology() {
  return (
    <div className="bg-surface relative" id="methodology">
      
      {/* Section 1: Scroll Highlight */}
      <section className="py-[15vh] px-lg max-w-4xl mx-auto min-h-screen flex flex-col justify-center relative z-20 bg-surface">
        <h2 className="font-display-sm text-display-sm text-primary mb-xl">Make your practice easier to run without compromising patient trust.</h2>
        <div className="font-display-sm text-display-sm-mobile md:text-display-sm leading-snug">
          <HighlightText text="A health practice does not need technology for its own sake. It needs systems that support the people already doing the work." />
          <HighlightText text="As practices grow, the work around clinical care can become harder to coordinate. Enquiries need follow-up. Referrals need tracking. Staff need clear handovers. Managers need to know what is happening without chasing updates. Sensitive information needs to be handled carefully. And if AI is being considered, the rules need to be clear before staff start experimenting." />
          <HighlightText text="Heutrix Labs starts by understanding how your practice actually works, then recommends practical improvements that are safe, maintainable and useful in daily operations." />
        </div>
      </section>

      {/* Section 2: Sticky Parallax */}
      <StickySection title="Start with the right level of support." bgColor="bg-surface-container-low">
        <div className="space-y-xl bg-white p-xl rounded-xxl shadow-xl border border-slate-200">
          <div>
            <h3 className="font-headline-sm text-headline-sm text-primary mb-sm">1. Free fit call</h3>
            <p className="font-body-lg text-body-lg text-on-surface-variant">A short call to understand the workflow or operational problem, confirm whether Heutrix Labs is likely to help and recommend the most practical next step. We may recommend a diagnostic, a defined build, a safe AI review, a tailored scope or no project if the problem is not a good fit.</p>
          </div>
          <div>
            <h3 className="font-headline-sm text-headline-sm text-primary mb-sm">2. Diagnostic where the opportunity is unclear</h3>
            <p className="font-body-lg text-body-lg text-on-surface-variant">If the workflow needs more investigation, the Workflow Diagnostic helps answer: what is happening now, where is the friction, what is the best opportunity to improve, what risks need to be considered and what should be built first?</p>
          </div>
          <div>
            <h3 className="font-headline-sm text-headline-sm text-primary mb-sm">3. Build where there is a clear opportunity</h3>
            <p className="font-body-lg text-body-lg text-on-surface-variant">Where the opportunity is clear, we move into a focused implementation with a written scope, agreed deliverables and practical handover.</p>
          </div>
        </div>
      </StickySection>

      {/* Section 3: Sticky Parallax */}
      <StickySection title="Workflow first. Technology second." bgColor="bg-surface">
        <div className="bg-surface-container p-xl rounded-xxl border border-slate-200">
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs does not start by pushing software or AI. We start by understanding the workflow, the people involved, the information being handled, the decisions being made and the points where work gets stuck. Then we recommend the simplest useful improvement.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Our work is:</p>
          <ul className="grid sm:grid-cols-2 gap-sm mb-lg">
            {['practice-led', 'operationally practical', 'privacy-aware', 'safe-AI aware', 'commercially grounded', 'documented', 'tested with users', 'designed for handover', 'built to fit existing tools'].map((item, i) => (
              <li key={i} className="flex items-center gap-xs font-body-md text-body-md text-on-surface-variant">
                <span className="material-symbols-outlined text-secondary text-[18px]" data-icon="check">check</span> {item}
              </li>
            ))}
          </ul>
          <p className="font-body-lg text-body-lg text-primary font-medium border-l-4 border-secondary pl-md">We do not automate a workflow without first understanding why it matters, who relies on it and what could go wrong if it is changed poorly.</p>
        </div>
      </StickySection>

      {/* Section 4: Sticky Parallax */}
      <StickySection title="Safe AI support for health practice workflows." bgColor="bg-primary">
        <div className="text-on-primary space-y-md p-xl border border-white/10 rounded-xxl bg-white/5 backdrop-blur-md">
          <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">AI can be useful for drafting, summarising, organising information, preparing internal notes, extracting tasks and reducing repetitive admin. But in health and medical settings, AI also introduces serious risks if it is used without clear boundaries.</p>
          <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">Heutrix Labs helps practices introduce AI in a controlled and practical way. We focus on operational use cases, clear rules, data handling boundaries and human review.</p>
          <div className="p-lg bg-error-container text-error rounded-xl shadow-lg border border-error/20">
            <p className="font-body-md text-body-md font-medium">Heutrix Labs does not recommend putting identifiable patient, client, participant, staff or sensitive business information into publicly available generative AI tools. Any AI use involving personal or sensitive information requires careful review of purpose, consent, privacy notices, tool settings, data storage, access controls, human review and professional obligations.</p>
          </div>
          <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">Our safe AI work focuses on: approved AI use cases, prohibited AI use cases, sensitive information and data handling rules, human review points, staff guidance, prompt templates for approved uses, AI-supported operational workflows with clear controls, and practical adoption that respects patient trust.</p>
          <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">Heutrix Labs does not build diagnostic tools, treatment recommendation tools, clinical decision-making systems or medical-device software as part of its current services.</p>
          <p className="font-headline-sm text-headline-sm text-white border-t border-white/20 pt-md">AI should support human work, not replace clinical judgement, professional responsibility or management oversight.</p>
        </div>
      </StickySection>

      {/* Section 5 & 6 (Standard layout to avoid over-animating) */}
      <section className="py-xxl px-lg max-w-4xl mx-auto space-y-xxl relative z-20 bg-surface">
        <div>
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Better visibility for day-to-day practice decisions.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Good operational visibility helps practice owners and managers understand what is happening without relying on scattered spreadsheets, manual updates or one person’s memory.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">We can help create clearer views of patient enquiries, referral status, recall and follow-up activity, onboarding progress, internal admin tasks, document collection, staff handovers, team workload, operational KPIs, management reporting, and recurring process bottlenecks.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant font-bold text-primary border-l-4 border-secondary pl-md">The goal is not just to display information. The goal is to help the right person see what needs attention.</p>
        </div>

        <div className="bg-surface-container p-xl rounded-xl border border-slate-200">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Selected NDIS operational workflow support.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs can support selected NDIS providers with operational workflows such as intake, onboarding, internal admin tracking and service coordination.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">This work is separate from NDIS registration readiness, evidence preparation, audit readiness, mock audit support, compliance gap assessments and assurance services.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Where a provider needs NDIS registration readiness, audit-readiness support, evidence preparation, mock audit support, compliance gap assessment or assurance services, that work is outside the Heutrix Labs scope and must be arranged separately with an appropriate provider. Official NDIS registration audits must be conducted by approved quality auditors.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs work does not guarantee registration, audit success or NDIS Commission approval.</p>
          <a className="inline-flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md mt-sm" href="#contact">View NDIS operational workflow support</a>
        </div>

        <div className="text-center mx-auto py-xl">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Not sure what workflow to improve first?</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-lg">Start with a free fit call. If there is a good fit, we may recommend a Workflow Diagnostic to identify the most practical improvement opportunity before you commit to a build.</p>
          <a className="inline-flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md" href="#contact">Book a free fit call</a>
        </div>
      </section>
    </div>
  );
}
"""

components['Services.jsx'] = """import React from 'react';
import { motion } from 'framer-motion';

export default function Services() {
  const container = {
    hidden: { opacity: 0 },
    show: { opacity: 1, transition: { staggerChildren: 0.1 } }
  };
  const card = {
    hidden: { opacity: 0, y: 40, scale: 0.95 },
    show: { opacity: 1, y: 0, scale: 1, transition: { type: "spring", stiffness: 60, damping: 15 } }
  };

  const servicesData = [
    { 
      icon: 'troubleshoot', 
      title: 'Workflow Diagnostic', 
      desc: 'Find the workflow worth improving first. A structured review for practices that know something is taking too much time, creating risk or causing avoidable friction, but are not yet sure what should be changed first. We review the current workflow, identify pain points, assess practical improvement options and recommend a clear next step before you commit to a solution or implementation build.', 
      link: 'Start with a Workflow Diagnostic', bg: 'bg-surface-container', text: 'text-primary' 
    },
    { 
      icon: 'auto_mode', 
      title: 'Workflow Improvement Build', 
      desc: 'Improve one important admin or operational workflow. A focused build where we improve a defined workflow such as patient enquiry follow-up, referral tracking, onboarding, recall coordination, document collection, internal requests, reporting preparation or routine admin tracking. The outcome may be a better process, form, tracker, reminder system, visibility view, automation between existing tools or a lightweight internal system.', 
      link: 'Improve a workflow', bg: 'bg-surface-container', text: 'text-primary' 
    },
    { 
      icon: 'visibility', 
      title: 'Practice Visibility Build', 
      desc: 'See what needs attention without chasing updates. For practices that need a clearer view of enquiries, referrals, recalls, tasks, workload, onboarding, document collection or management reporting. The goal is not to create a dashboard for its own sake. The goal is to help the right person see what needs attention, what is waiting and where follow-up is needed.', 
      link: 'Improve practice visibility', bg: 'bg-surface-container', text: 'text-primary' 
    },
    { 
      icon: 'security', 
      title: 'Safe AI Use Pack', 
      desc: 'Set safe rules before AI becomes part of practice work. For practices that want to explore AI carefully, or already have staff using AI tools informally. We help define appropriate and inappropriate use cases, sensitive information rules, human review steps, staff guidance and practical boundaries so AI supports the practice without undermining privacy, trust or professional judgement.', 
      link: 'Set up safe AI use', bg: 'bg-secondary-container', text: 'text-on-secondary-container', active: true 
    },
    { 
      icon: 'dashboard_customize', 
      title: 'Tailored Internal Workflow System', 
      desc: "For workflows that need something more tailored. For practices that need a more tailored internal workflow than a standard tracker, form or visibility build. This may include a lightweight internal request system, a structured admin workflow, a custom operations view or an approved AI-supported admin step with clear controls. This work is only recommended after we understand the workflow, the information involved, who will use it, what needs to be reviewed by a person and what risks need to be controlled.", 
      link: 'Scope a tailored workflow system', bg: 'bg-surface-container', text: 'text-primary' 
    }
  ];

  return (
    <section className="py-xxl px-lg bg-surface relative z-20" id="services">
      <div className="max-w-container-max mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="mb-xxl text-center max-w-3xl mx-auto">
          <h2 className="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-md">Practical ways we can help.</h2>
        </motion.div>

        <motion.div variants={container} initial="hidden" whileInView="show" viewport={{ once: true, amount: 0.1 }} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-lg">
          {servicesData.map((s, i) => (
            <motion.div 
              key={i} 
              variants={card} 
              className="glass-card p-xl rounded-xl border border-slate-200 hover:shadow-2xl transition-all group flex flex-col h-full transform-gpu origin-center"
              whileHover={{ scale: 1.02, y: -5 }}
            >
              <div className={`w-14 h-14 ${s.bg} rounded-full flex items-center justify-center ${s.text} mb-lg group-hover:scale-110 transition-transform shrink-0`}>
                <span className="material-symbols-outlined text-[32px]" data-icon={s.icon}>{s.icon}</span>
              </div>
              <h3 className="font-headline-sm text-headline-sm mb-sm text-primary">{s.title}</h3>
              <p className="font-body-md text-body-md text-on-surface-variant mb-xl">{s.desc}</p>
              <div className="mt-auto">
                <a className="flex items-center gap-sm text-primary font-bold hover:underline" href="#contact">{s.link} <span className="material-symbols-outlined" data-icon="chevron_right">chevron_right</span></a>
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
"""

for name, content in components.items():
    with open(f'src/components/{name}', 'w') as f:
        f.write(content)

