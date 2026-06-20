import React, { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

const StickySection = ({ title, children, bgColor = "bg-surface" }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start start", "end end"]
  });

  const titleOpacity = useTransform(scrollYProgress, [0, 0.1, 0.9, 1], [0, 1, 1, 0]);
  const titleY = useTransform(scrollYProgress, [0, 0.1, 0.9, 1], [50, 0, 0, -50]);
  
  const contentOpacity = useTransform(scrollYProgress, [0.1, 0.25, 0.85, 1], [0, 1, 1, 0]);
  const contentY = useTransform(scrollYProgress, [0.1, 0.25, 0.85, 1], [100, 0, 0, -100]);
  const contentFilter = useTransform(scrollYProgress, [0.1, 0.25, 0.85, 1], ["blur(12px)", "blur(0px)", "blur(0px)", "blur(12px)"]);

  const titleColor = bgColor === "bg-primary" ? "text-white" : "text-primary";

  return (
    <section ref={ref} className={`h-[250vh] ${bgColor} relative z-20`}>
      <div className="sticky top-0 h-screen flex flex-col md:flex-row items-center justify-center px-lg gap-xl max-w-container-max mx-auto overflow-hidden">
        <motion.div style={{ opacity: titleOpacity, y: titleY }} className="flex-1">
          <h2 className={`font-headline-md text-headline-md ${titleColor}`}>{title}</h2>
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
      
      {/* Section 1: Cinematic Typography Blocks */}
      <section className="py-xxl px-lg max-w-5xl mx-auto space-y-[15vh] relative z-20 bg-surface my-[10vh]">
        <motion.div initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }} viewport={{ once: true, amount: 0.5 }}>
          <h2 className="font-headline-md text-headline-md text-primary mb-md">Make your practice easier to run without compromising patient trust.</h2>
          <p className="font-headline-md text-headline-md text-on-surface-variant font-normal">
            A health practice does not need technology for its own sake. It needs systems that support the people already doing the work.
          </p>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }} viewport={{ once: true, amount: 0.5 }}>
          <p className="font-headline-md text-headline-md text-on-surface-variant font-normal">
            As practices grow, the work around clinical care can become harder to coordinate. Enquiries need follow-up. Referrals need tracking. Staff need clear handovers. Managers need to know what is happening without chasing updates. Sensitive information needs to be handled carefully. And if AI is being considered, the rules need to be clear before staff start experimenting.
          </p>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }} viewport={{ once: true, amount: 0.5 }}>
          <p className="font-headline-md text-headline-md text-on-surface-variant font-normal">
            Heutrix Labs starts by understanding how your practice actually works, then recommends practical improvements that are safe, maintainable and useful in daily operations.
          </p>
        </motion.div>
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

      {/* Section 4: Side-by-Side Safe AI Layout (No fixed height lock) */}
      <section className="bg-primary text-on-primary py-xxl px-lg relative z-20">
        <div className="max-w-container-max mx-auto grid md:grid-cols-12 gap-xl">
          <div className="md:col-span-5 relative">
            <div className="sticky top-32">
              <h2 className="font-headline-md text-headline-md text-white">Safe AI support for health practice workflows.</h2>
            </div>
          </div>
          <div className="md:col-span-7 space-y-xl">
            <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="p-xl border border-white/10 rounded-xxl bg-white/5 backdrop-blur-md">
              <p className="font-body-lg text-body-lg text-inverse-on-surface mb-lg">AI can be useful for drafting, summarising, organising information, preparing internal notes, extracting tasks and reducing repetitive admin. But in health and medical settings, AI also introduces serious risks if it is used without clear boundaries.</p>
              <p className="font-body-lg text-body-lg text-inverse-on-surface">Heutrix Labs helps practices introduce AI in a controlled and practical way. We focus on operational use cases, clear rules, data handling boundaries and human review.</p>
            </motion.div>

            <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="p-xl bg-error-container text-error rounded-xxl shadow-lg border border-error/20">
              <p className="font-body-lg text-body-lg font-medium">Heutrix Labs does not recommend putting identifiable patient, client, participant, staff or sensitive business information into publicly available generative AI tools. Any AI use involving personal or sensitive information requires careful review of purpose, consent, privacy notices, tool settings, data storage, access controls, human review and professional obligations.</p>
            </motion.div>

            <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="p-xl border border-white/10 rounded-xxl bg-white/5 backdrop-blur-md">
              <p className="font-body-lg text-body-lg text-inverse-on-surface mb-lg">Our safe AI work focuses on: approved AI use cases, prohibited AI use cases, sensitive information and data handling rules, human review points, staff guidance, prompt templates for approved uses, AI-supported operational workflows with clear controls, and practical adoption that respects patient trust.</p>
              <p className="font-body-lg text-body-lg text-inverse-on-surface">Heutrix Labs does not build diagnostic tools, treatment recommendation tools, clinical decision-making systems or medical-device software as part of its current services.</p>
            </motion.div>

            <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }}>
              <p className="font-headline-sm text-headline-sm text-secondary-fixed border-l-4 border-secondary-fixed pl-md">AI should support human work, not replace clinical judgement, professional responsibility or management oversight.</p>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Section 5 & 6 */}
      <section className="py-xxl px-lg max-w-4xl mx-auto space-y-xxl relative z-20 bg-surface mt-xl">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }}>
          <h2 className="font-headline-md text-headline-md text-primary mb-md">Better visibility for day-to-day practice decisions.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Good operational visibility helps practice owners and managers understand what is happening without relying on scattered spreadsheets, manual updates or one person’s memory.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">We can help create clearer views of patient enquiries, referral status, recall and follow-up activity, onboarding progress, internal admin tasks, document collection, staff handovers, team workload, operational KPIs, management reporting, and recurring process bottlenecks.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant font-bold text-primary border-l-4 border-secondary pl-md">The goal is not just to display information. The goal is to help the right person see what needs attention.</p>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="bg-surface-container p-xl rounded-xl border border-slate-200">
          <h2 className="font-headline-md text-headline-md text-primary mb-md">Selected NDIS operational workflow support.</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs can support selected NDIS providers with operational workflows such as intake, onboarding, internal admin tracking and service coordination.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">This work is separate from NDIS registration readiness, evidence preparation, audit readiness, mock audit support, compliance gap assessments and assurance services.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Where a provider needs NDIS registration readiness, audit-readiness support, evidence preparation, mock audit support, compliance gap assessment or assurance services, that work is outside the Heutrix Labs scope and must be arranged separately with an appropriate provider. Official NDIS registration audits must be conducted by approved quality auditors.</p>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-md">Heutrix Labs work does not guarantee registration, audit success or NDIS Commission approval.</p>
          <a className="inline-flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md mt-sm" href="#contact">View NDIS operational workflow support</a>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="text-center mx-auto py-xl">
          <h2 className="font-headline-md text-headline-md text-primary mb-md">Not sure what workflow to improve first?</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant mb-lg">Start with a free fit call. If there is a good fit, we may recommend a Workflow Diagnostic to identify the most practical improvement opportunity before you commit to a build.</p>
          <a className="inline-flex items-center justify-center gap-sm bg-primary text-on-primary px-xl py-lg rounded-xl font-headline-sm hover:opacity-90 transition-all shadow-md" href="#contact">Book a free fit call</a>
        </motion.div>
      </section>
    </div>
  );
}
