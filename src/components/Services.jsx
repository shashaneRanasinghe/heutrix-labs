import React from 'react';
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
