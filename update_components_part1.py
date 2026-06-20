import os

components = {}

components['Hero.jsx'] = """import React from 'react';
import { motion } from 'framer-motion';

export default function Hero() {
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: { staggerChildren: 0.15, delayChildren: 0.2 }
    }
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
          <motion.p variants={item} className="font-body-lg text-body-lg text-on-surface-variant mb-xl max-w-xl">
            We help reduce repeated admin, improve follow-up, make important work easier to see and set safe rules for AI use where it genuinely helps.
          </motion.p>
          <motion.div variants={item} className="flex flex-col sm:flex-row gap-md">
            <a className="flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md group" href="#contact">
              Book a free fit call
              <span className="material-symbols-outlined group-hover:translate-x-1 transition-transform" data-icon="arrow_forward">arrow_forward</span>
            </a>
            <a className="flex items-center justify-center gap-sm border-2 border-primary text-primary px-xl py-lg rounded-xl font-headline-sm hover:bg-primary hover:text-on-primary transition-all" href="#services">
              View services
            </a>
          </motion.div>
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

components['Problem.jsx'] = """import React, { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

export default function Problem() {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"]
  });

  const titleOpacity = useTransform(scrollYProgress, [0, 0.15], [1, 0]);
  const titleY = useTransform(scrollYProgress, [0, 0.15], [0, -50]);

  const step1Opacity = useTransform(scrollYProgress, [0.1, 0.2, 0.35, 0.45], [0, 1, 1, 0]);
  const step1Y = useTransform(scrollYProgress, [0.1, 0.2, 0.35, 0.45], [50, 0, 0, -50]);
  const step1Scale = useTransform(scrollYProgress, [0.1, 0.2], [0.9, 1]);

  const step2Opacity = useTransform(scrollYProgress, [0.4, 0.5, 0.65, 0.75], [0, 1, 1, 0]);
  const step2Y = useTransform(scrollYProgress, [0.4, 0.5, 0.65, 0.75], [50, 0, 0, -50]);
  const step2Scale = useTransform(scrollYProgress, [0.4, 0.5], [0.9, 1]);

  const step3Opacity = useTransform(scrollYProgress, [0.7, 0.8, 0.95, 1], [0, 1, 1, 1]);
  const step3Y = useTransform(scrollYProgress, [0.7, 0.8, 0.95, 1], [50, 0, 0, 0]);
  const step3Scale = useTransform(scrollYProgress, [0.7, 0.8], [0.9, 1]);

  return (
    <section ref={containerRef} className="bg-primary text-on-primary h-[300vh]" id="problem">
      <div className="sticky top-0 h-screen flex flex-col justify-center items-center px-lg overflow-hidden">
        
        <motion.div style={{ opacity: titleOpacity, y: titleY }} className="absolute top-[20%] text-center px-lg w-full max-w-4xl">
          <h2 className="font-headline-md text-headline-md mb-md">When important work is spread across memory, inboxes and spreadsheets, even capable teams can lose visibility.</h2>
        </motion.div>

        <div className="relative w-full max-w-4xl h-[400px]">
          <motion.div style={{ opacity: step1Opacity, y: step1Y, scale: step1Scale }} className="absolute top-1/2 -translate-y-1/2 left-0 w-full flex flex-col md:flex-row gap-lg items-start">
            <span className="font-display-lg text-secondary-fixed-dim shrink-0">01</span>
            <div>
              <h3 className="font-headline-sm text-headline-sm mb-sm text-white">Scattered Administration</h3>
              <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">Patient enquiries are followed up differently. Routine admin steps depend on memory, inbox searches, or one person's local spreadsheet.</p>
            </div>
          </motion.div>

          <motion.div style={{ opacity: step2Opacity, y: step2Y, scale: step2Scale }} className="absolute top-1/2 -translate-y-1/2 left-0 w-full flex flex-col md:flex-row gap-lg items-start">
            <span className="font-display-lg text-secondary-fixed-dim shrink-0">02</span>
            <div>
              <h3 className="font-headline-sm text-headline-sm mb-sm text-white">Tracking Blindspots</h3>
              <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">Referrals, recalls, and document requests are hard to track end-to-end. Managers cannot easily see workload or bottlenecks without chasing updates.</p>
            </div>
          </motion.div>

          <motion.div style={{ opacity: step3Opacity, y: step3Y, scale: step3Scale }} className="absolute top-1/2 -translate-y-1/2 left-0 w-full flex flex-col md:flex-row gap-lg items-start">
            <span className="font-display-lg text-secondary-fixed-dim shrink-0">03</span>
            <div>
              <h3 className="font-headline-sm text-headline-sm mb-sm text-white">Informal AI Risks</h3>
              <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">AI tools are being used informally. Without clear rules and safe pipelines, your patient trust and sensitive information are at risk.</p>
            </div>
          </motion.div>
        </div>
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
    show: {
      opacity: 1,
      transition: { staggerChildren: 0.1 }
    }
  };

  const card = {
    hidden: { opacity: 0, y: 40, scale: 0.95 },
    show: { opacity: 1, y: 0, scale: 1, transition: { type: "spring", stiffness: 60, damping: 15 } }
  };

  const servicesData = [
    { icon: 'troubleshoot', title: 'Workflow Diagnostic', desc: 'Find the workflow worth improving first. A structured review for practices that know something is causing friction.', price: 'From $1,500 ex GST', link: 'Diagnostic', bg: 'bg-surface-container', text: 'text-primary' },
    { icon: 'auto_mode', title: 'Workflow Improvement Build', desc: 'Improve one important admin or operational workflow using trackers, reminders, or automations.', price: 'From $4,500 ex GST', link: 'Improve a workflow', bg: 'bg-surface-container', text: 'text-primary' },
    { icon: 'visibility', title: 'Practice Visibility Build', desc: 'See what needs attention without chasing updates. A clearer view of enquiries, tasks, and follow-ups.', price: 'From $4,500 ex GST', link: 'Improve practice visibility', bg: 'bg-surface-container', text: 'text-primary' },
    { icon: 'security', title: 'Safe AI Use Pack', desc: 'Set safe rules before AI becomes part of practice work. Protect patient trust and sensitive information.', price: 'From $4,800 ex GST', link: 'Set up safe AI use', bg: 'bg-secondary-container', text: 'text-on-secondary-container', active: true },
    { icon: 'dashboard_customize', title: 'Tailored Internal Workflow', desc: "For workflows that need something more tailored, like a custom request management system or structured operations view.", price: 'From $9,500 ex GST', link: 'Scope a tailored system', bg: 'bg-surface-container', text: 'text-primary' },
    { icon: 'health_metrics', title: 'NDIS Operations Support', desc: 'Operational workflow support for selected NDIS providers for intake, onboarding, and admin tracking.', price: 'From $6,500 ex GST', link: 'NDIS operational support', bg: 'bg-primary', text: 'text-on-primary' }
  ];

  return (
    <section className="py-xxl px-lg bg-surface" id="services">
      <div className="max-w-container-max mx-auto">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true, amount: 0.3 }}
          className="mb-xxl text-center max-w-3xl mx-auto"
        >
          <h2 className="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-md">Practical ways we can help.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant">We review current workflows, identify practical improvement opportunities and build simple, maintainable systems.</p>
        </motion.div>

        <motion.div 
          variants={container}
          initial="hidden"
          whileInView="show"
          viewport={{ once: true, amount: 0.1 }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-lg"
        >
          {servicesData.map((s, i) => (
            <motion.div key={i} variants={card} className="glass-card p-xl rounded-xl border border-slate-200 hover:shadow-xl transition-all group flex flex-col h-full">
              <div className={`w-14 h-14 ${s.bg} rounded-full flex items-center justify-center ${s.text} mb-lg group-hover:scale-110 transition-transform`}>
                <span className="material-symbols-outlined text-[32px]" data-icon={s.icon}>{s.icon}</span>
              </div>
              <h3 className="font-headline-sm text-headline-sm mb-sm text-primary">{s.title}</h3>
              <p className="font-body-md text-body-md text-on-surface-variant mb-xl">{s.desc}</p>
              <div className="mt-auto">
                <p className="font-label-md text-label-md text-secondary mb-md">{s.price}</p>
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

