import os

components = {}

components['Hero.jsx'] = """import React from 'react';
import { motion } from 'framer-motion';

export default function Hero() {
  const container = {
    hidden: { opacity: 0 },
    show: { opacity: 1, transition: { staggerChildren: 0.15, delayChildren: 0.2 } }
  };
  const item = {
    hidden: { opacity: 0, y: 30 },
    show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 70, damping: 15 } }
  };

  return (
    <section className="relative overflow-hidden min-h-[795px] flex items-center px-lg py-xxl" id="home">
      <div className="max-w-container-max mx-auto w-full relative z-10 grid lg:grid-cols-2 gap-xl items-center">
        <motion.div variants={container} initial="hidden" whileInView="show" viewport={{ once: true, amount: 0.3 }}>
          <motion.div variants={item} className="inline-flex items-center gap-sm bg-secondary-container text-on-secondary-container px-md py-xs rounded-full mb-lg shadow-sm border border-on-secondary-container/10">
            <span className="material-symbols-outlined text-[18px]" data-icon="verified">verified</span>
            <span className="font-label-sm text-label-sm uppercase tracking-widest">Workflow improvement for Australian health practices</span>
          </motion.div>
          <motion.h1 variants={item} className="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-md leading-tight">
            Workflow improvement and safe AI support for Australian health practices.
          </motion.h1>
          <motion.p variants={item} className="font-body-lg text-body-lg text-on-surface-variant mb-md max-w-xl">
            Heutrix Labs helps allied health, dental, medical and specialist practices improve the operational work around patient care.
          </motion.p>
          <motion.p variants={item} className="font-body-lg text-body-lg text-on-surface-variant mb-md max-w-xl">
            We help reduce repeated admin, improve follow-up, make important work easier to see and set safe rules for AI use where it genuinely helps.
          </motion.p>
          <motion.p variants={item} className="font-body-lg text-body-lg text-on-surface-variant mb-xl max-w-xl">
            We start with how your practice actually works, then recommend practical improvements such as clearer workflows, better tracking, safer AI rules, automation between existing tools, visibility views or lightweight internal systems.
          </motion.p>
          <motion.div variants={item} className="flex flex-col sm:flex-row gap-md mb-md">
            <a className="flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md group" href="#contact">
              Book a free fit call
              <span className="material-symbols-outlined group-hover:translate-x-1 transition-transform" data-icon="arrow_forward">arrow_forward</span>
            </a>
            <a className="flex items-center justify-center gap-sm border-2 border-primary text-primary px-xl py-lg rounded-xl font-headline-sm hover:bg-primary hover:text-on-primary transition-all" href="#services">
              View services
            </a>
          </motion.div>
          <motion.p variants={item} className="font-body-sm text-body-sm text-on-surface-variant italic max-w-xl">
            For established practices that want clearer workflows, safer AI use and better day-to-day operational visibility without disrupting patient care.
          </motion.p>
        </motion.div>
        <motion.div 
          initial={{ opacity: 0, scale: 1.05 }}
          whileInView={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1], delay: 0.4 }}
          viewport={{ once: true, amount: 0.3 }}
          className="hidden lg:block"
        >
          <div className="relative p-lg rounded-xxl overflow-hidden bg-white shadow-2xl border border-slate-200">
            <img alt="Operations Dashboard" className="rounded-xl w-full h-[500px] object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCZE6OKQ5bJ9PCNRZbFYz_Wv9wn5UwhHvktLaV1sU0ihN5G_3ly6hMBVxeRO35AU-eyp0c7FNEBSCbSXNHUF1XcFTFi74M6xPGnkf9qhKDF__rPoWWYGTxalDg69nzb6HFMbWtYsedzAj0U_KLeiim0JKwhdi9u820K8pCe3f861GgGk-EW1Nyq8C7VojOMp0BUj7YFQsf6l0cPfFYlYXrg2LPkdbVh3aqHGnoo-sKY-TvycYmoT0mpwoDn5tBAY3NvWJKrPaus_t85"/>
            <div className="absolute bottom-12 left-12 right-12 bg-white/90 backdrop-blur-md p-lg rounded-xl border border-slate-200 shadow-xl">
              <div className="flex items-center gap-md">
                <div className="w-12 h-12 rounded-full bg-secondary-container flex items-center justify-center text-on-secondary-container">
                  <span className="material-symbols-outlined" data-icon="visibility">visibility</span>
                </div>
                <div>
                  <p className="font-label-md text-label-md text-primary">Clearer Workflows</p>
                  <p className="font-body-sm text-body-sm text-on-surface-variant">Without disrupting patient care</p>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
"""

components['Problem.jsx'] = """import React from 'react';
import { motion } from 'framer-motion';

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

  return (
    <section className="py-xxl px-lg bg-surface-container-low" id="problem">
      <div className="max-w-container-max mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl mb-xl">
          <h2 className="font-display-md text-display-md-mobile md:text-display-md text-primary mb-md">When important work is spread across memory, inboxes and spreadsheets, even capable teams can lose visibility.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant">
            Many practice teams are highly capable, but the systems around them have not always kept up with growth, staff changes, patient demand or disconnected tools. Heutrix Labs helps identify where important admin and operational work needs clearer ownership, tracking, reminders, handover or review.
          </p>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.2 }} viewport={{ once: true, amount: 0.2 }} className="bg-white p-xl rounded-xxl shadow-sm border border-slate-200 mb-xl">
          <h3 className="font-headline-sm text-headline-sm text-primary mb-lg">You may notice:</h3>
          <ul className="grid md:grid-cols-2 gap-x-lg gap-y-md">
            {issues.map((issue, i) => (
              <li key={i} className="flex items-start gap-sm">
                <span className="material-symbols-outlined text-secondary shrink-0 mt-1" data-icon="radio_button_unchecked">radio_button_unchecked</span>
                <span className="font-body-md text-body-md text-on-surface-variant">{issue}</span>
              </li>
            ))}
          </ul>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.4 }} viewport={{ once: true, amount: 0.2 }}>
          <p className="font-body-lg text-body-lg text-primary font-medium max-w-4xl border-l-4 border-secondary pl-lg">
            Heutrix Labs helps turn these pressure points into clearer workflows, practical tracking systems, safer AI practices and better visibility for day-to-day decisions.
          </p>
        </motion.div>
      </div>
    </section>
  );
}
"""

components['Methodology.jsx'] = """import React from 'react';
import { motion } from 'framer-motion';

export default function Methodology() {
  return (
    <section className="py-xxl px-lg bg-surface" id="methodology">
      <div className="max-w-container-max mx-auto space-y-xxl">
        
        {/* Section 1 */}
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Make your practice easier to run without compromising patient trust.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">
            A health practice does not need technology for its own sake. It needs systems that support the people already doing the work.
          </p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">
            As practices grow, the work around clinical care can become harder to coordinate. Enquiries need follow-up. Referrals need tracking. Staff need clear handovers. Managers need to know what is happening without chasing updates. Sensitive information needs to be handled carefully. And if AI is being considered, the rules need to be clear before staff start experimenting.
          </p>
          <p className="font-body-lg text-body-lg text-on-surface-variant">
            Heutrix Labs starts by understanding how your practice actually works, then recommends practical improvements that are safe, maintainable and useful in daily operations.
          </p>
        </motion.div>

        {/* Section 2 */}
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Start with the right level of support.</h2>
          <div className="space-y-lg">
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
        </motion.div>

        {/* Section 3 */}
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Workflow first. Technology second.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs does not start by pushing software or AI. We start by understanding the workflow, the people involved, the information being handled, the decisions being made and the points where work gets stuck. Then we recommend the simplest useful improvement.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Our work is:</p>
          <ul className="grid sm:grid-cols-2 md:grid-cols-3 gap-sm mb-md">
            {['practice-led', 'operationally practical', 'privacy-aware', 'safe-AI aware', 'commercially grounded', 'documented', 'tested with users', 'designed for handover', 'built to fit existing tools'].map((item, i) => (
              <li key={i} className="flex items-center gap-xs font-body-md text-body-md text-on-surface-variant">
                <span className="material-symbols-outlined text-secondary text-[18px]" data-icon="check">check</span> {item}
              </li>
            ))}
          </ul>
          <p className="font-body-lg text-body-lg text-on-surface-variant">We do not automate a workflow without first understanding why it matters, who relies on it and what could go wrong if it is changed poorly.</p>
        </motion.div>

        {/* Section 4 */}
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Safe AI support for health practice workflows.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">AI can be useful for drafting, summarising, organising information, preparing internal notes, extracting tasks and reducing repetitive admin. But in health and medical settings, AI also introduces serious risks if it is used without clear boundaries.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs helps practices introduce AI in a controlled and practical way. We focus on operational use cases, clear rules, data handling boundaries and human review.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md font-medium p-md bg-error-container/20 border-l-4 border-error rounded-r-lg">Heutrix Labs does not recommend putting identifiable patient, client, participant, staff or sensitive business information into publicly available generative AI tools. Any AI use involving personal or sensitive information requires careful review of purpose, consent, privacy notices, tool settings, data storage, access controls, human review and professional obligations.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Our safe AI work focuses on: approved AI use cases, prohibited AI use cases, sensitive information and data handling rules, human review points, staff guidance, prompt templates for approved uses, AI-supported operational workflows with clear controls, and practical adoption that respects patient trust.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs does not build diagnostic tools, treatment recommendation tools, clinical decision-making systems or medical-device software as part of its current services.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant font-bold">AI should support human work, not replace clinical judgement, professional responsibility or management oversight.</p>
        </motion.div>

        {/* Section 5 */}
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Better visibility for day-to-day practice decisions.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Good operational visibility helps practice owners and managers understand what is happening without relying on scattered spreadsheets, manual updates or one person’s memory.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">We can help create clearer views of patient enquiries, referral status, recall and follow-up activity, onboarding progress, internal admin tasks, document collection, staff handovers, team workload, operational KPIs, management reporting, and recurring process bottlenecks.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant font-bold text-primary">The goal is not just to display information. The goal is to help the right person see what needs attention.</p>
        </motion.div>

        {/* Section 6 */}
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl bg-surface-container p-xl rounded-xl border border-slate-200">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Selected NDIS operational workflow support.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs can support selected NDIS providers with operational workflows such as intake, onboarding, internal admin tracking and service coordination.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">This work is separate from NDIS registration readiness, evidence preparation, audit readiness, mock audit support, compliance gap assessments and assurance services.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Where a provider needs NDIS registration readiness, audit-readiness support, evidence preparation, mock audit support, compliance gap assessment or assurance services, that work is outside the Heutrix Labs scope and must be arranged separately with an appropriate provider. Official NDIS registration audits must be conducted by approved quality auditors.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs work does not guarantee registration, audit success or NDIS Commission approval.</p>
          <a className="inline-flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md mt-sm" href="#contact">View NDIS operational workflow support</a>
        </motion.div>

        {/* Section 7 */}
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl text-center mx-auto py-xl">
          <h2 className="font-display-sm text-display-sm text-primary mb-md">Not sure what workflow to improve first?</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-lg">Start with a free fit call. If there is a good fit, we may recommend a Workflow Diagnostic to identify the most practical improvement opportunity before you commit to a build.</p>
          <a className="inline-flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md" href="#contact">Book a free fit call</a>
        </motion.div>
      </div>
    </section>
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
    <section className="py-xxl px-lg bg-surface" id="services">
      <div className="max-w-container-max mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="mb-xxl text-center max-w-3xl mx-auto">
          <h2 className="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-md">Practical ways we can help.</h2>
        </motion.div>

        <motion.div variants={container} initial="hidden" whileInView="show" viewport={{ once: true, amount: 0.1 }} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-lg">
          {servicesData.map((s, i) => (
            <motion.div key={i} variants={card} className="glass-card p-xl rounded-xl border border-slate-200 hover:shadow-xl transition-all group flex flex-col h-full">
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

components['App.jsx'] = """import React, { useEffect, useState } from 'react';
import Navbar from './Navbar';
import Hero from './Hero';
import Problem from './Problem';
import Services from './Services';
import Methodology from './Methodology';
import Checklist from './Checklist';
import About from './About';
import FAQ from './FAQ';
import Contact from './Contact';
import Footer from './Footer';

function App() {
  const [activeSection, setActiveSection] = useState('home');

  useEffect(() => {
    const observerOptions = {
      root: null,
      rootMargin: '-40% 0px -40% 0px',
      threshold: 0
    };

    const observerCallback = (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          setActiveSection(entry.target.id);
        }
      });
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);
    const sections = document.querySelectorAll('section[id]');
    
    sections.forEach((section) => observer.observe(section));

    return () => observer.disconnect();
  }, []);

  return (
    <div className="min-h-screen bg-surface font-body-lg text-on-surface antialiased selection:bg-secondary/30 selection:text-primary scroll-smooth">
      <Navbar activeSection={activeSection} />
      
      <main>
        <Hero />
        <Problem />
        <Services />
        <Methodology />
        <Checklist />
        <About />
        <FAQ />
        <Contact />
      </main>

      <Footer />
    </div>
  );
}

export default App;
"""

for name, content in components.items():
    if name == 'App.jsx':
        with open(f'src/{name}', 'w') as f:
            f.write(content)
    else:
        with open(f'src/components/{name}', 'w') as f:
            f.write(content)

