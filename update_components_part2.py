import os

components = {}

components['Checklist.jsx'] = """import React, { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

export default function Checklist() {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start end", "end start"]
  });

  const parallaxY = useTransform(scrollYProgress, [0, 1], [50, -50]);

  return (
    <section className="py-xxl px-lg" id="checklist" ref={containerRef}>
      <motion.div 
        initial={{ opacity: 0, scale: 0.95 }}
        whileInView={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.8 }}
        viewport={{ once: true }}
        className="max-w-container-max mx-auto bg-primary text-on-primary rounded-xxl p-xl md:p-xxl relative overflow-hidden flex flex-col md:flex-row items-center gap-xl"
      >
        <div className="relative z-10 flex-1">
          <h2 className="font-display-lg text-display-lg-mobile md:text-display-lg mb-md">Download the Practice Workflow Opportunity Checklist</h2>
          <p className="font-body-lg text-body-lg text-on-primary-fixed-variant mb-xl">Find the admin and operational workflows your practice should stop managing manually. Use this checklist to identify repeated admin, manual follow-up, duplicated data entry, reporting gaps, and unclear handovers.</p>
          <button className="bg-secondary-fixed text-on-secondary-fixed px-xl py-lg rounded-xl font-headline-sm hover:scale-105 transition-transform flex items-center gap-md">
            <span className="material-symbols-outlined" data-icon="download">download</span>
            Download the Checklist
          </button>
        </div>
        <div className="relative z-10 flex-1 hidden lg:block">
          <motion.div style={{ y: parallaxY }} className="bg-white/10 backdrop-blur-md p-lg rounded-xl border border-white/20 rotate-3 transform shadow-2xl">
            <img alt="Checklist Preview" className="rounded-lg w-full h-auto shadow-sm" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCPEz3ronE3xNYG45Wfa7YhUbGtQXxRpenB-kBWi1Ee1A7kxMAlEKNFZXX1ECOWMM1gA4irAYTFSzFu3V0_AuViKXAF9vIOrkuMW1KZWHX8_uZGpIPtyp7mPtZFei-X58JeR8o3xayU8CmXKLCvp6ew9UPOVMblg1zwIbH1rHeE3xL-eaEWtgwMcaxr-q3i0l8oMqic0PYPeTBjA2mzCK8ACBDaB2Ic4zN-HWSX1QLT-PTEETSWDcijo7ya9hAqj05jAojImtxsCCzo"/>
          </motion.div>
        </div>
      </motion.div>
    </section>
  );
}
"""

components['About.jsx'] = """import React from 'react';
import { motion } from 'framer-motion';

export default function About() {
  return (
    <section className="py-xxl px-lg bg-surface-container-low overflow-hidden" id="about">
      <div className="max-w-container-max mx-auto">
        <div className="grid lg:grid-cols-2 gap-xxl items-center">
          <motion.div initial={{ opacity: 0, x: -30 }} whileInView={{ opacity: 1, x: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.3 }}>
            <h2 className="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-md">"We diagnose before we build."</h2>
            <p className="font-body-lg text-body-lg text-on-surface-variant mb-lg">
              Good operational improvement starts with understanding the workflow. Before recommending a system, dashboard, automation or AI-supported workflow, we look at what triggers the process, who is involved, where work gets stuck, and what risks need to be controlled. Then we recommend the simplest useful solution.
            </p>
            <div className="p-lg bg-error-container text-on-error-container rounded-xl border-l-4 border-error mb-xl">
              <div className="flex items-start gap-md">
                <span className="material-symbols-outlined mt-1" data-icon="warning">warning</span>
                <div>
                  <p className="font-label-md text-label-md font-bold mb-xs">Clear service boundaries</p>
                  <p className="font-body-sm text-body-sm">
                    Heutrix Labs provides workflow improvement, safe AI support, practice visibility builds and operational systems. We do **NOT** provide clinical advice, medical advice, legal advice, financial advice, regulatory advice, official audit services, NDIS registration readiness, or compliance gap assessments.
                  </p>
                </div>
              </div>
            </div>
            <div className="flex items-center gap-lg">
              <div className="flex -space-x-3">
                <img alt="Team 1" className="w-12 h-12 rounded-full border-2 border-white" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD_FDpeGrj83O_E8dSV8puy049SMrnZP1KWY9CICQXfQpUmnaoJ1HKMvvk7nSMZQeTk2YWrZTmzqaZpb0XPur2m7CTWjJwqOE_6xunZFl0Zh3TJwB-Lnb4rfBoh0UYbl7t3KFi0cKoWJ7MX8Kr_UBTRocorXCLTcf5GpWMlCO1-h0zbUfOXsh0JiUGt1Knp3YXEOgQSiJg-wIc5-H6EGjPOMxrek2r3LQcHyFjXOpPAIv42riwpAYGjN5H0sm3BhZ0v9NkSFlqUw7Q4"/>
                <img alt="Team 2" className="w-12 h-12 rounded-full border-2 border-white" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBhGknVEQFeApSJYPmla1zIIqpSm2EE4GXcMy4urTBFk8J5vwy4fxcFYfoxwDGVjfd2iaQ91KChi6zOBAsQ23gPDFN81G3xrb84SHl_vzxNwhPgGQR2e-1SzuLJbiVBj6Hf1dJGM_qls2-6XBAm-75CQxqUCmZvSZdfXHLgPJyCHEZDsPr51hWKj4q9pxIOAqWal0xqSl8NF5dMK7xxTvY7-qR6kfHofYULF1k3x6jOnLzujuT6erJVyRA7HgBcxb0glIOQWWH78XUn"/>
                <img alt="Team 3" className="w-12 h-12 rounded-full border-2 border-white" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBVbGk5V7d77WyI_yuJOm4CgSXeWX--jLXEPC9S9uxjX_CjzRk630OaMaoez2NtqR9wUWwllN38vlX24v0jxO0OTPuZOUMww3rEDEJgGvCU-bzTwhWWu-kHTGeYbd-rFHKRIbMjHvbkEgQFe_DCmvjmE7Jxf5XbFug5sSHGIo2LkYwbpNyToQRriSx2YFl3e8y-xxKp5Humq6Z2RPfimZ5KDr0QH1J6XN7TZzMWvaAhJ4BR-EtPSi1A9nzBZwWR92PFUho6BBLqaSVq"/>
              </div>
              <span className="font-label-md text-label-md text-on-surface-variant">Trusted by Australian Practices</span>
            </div>
          </motion.div>
          <motion.div initial={{ opacity: 0, x: 30 }} whileInView={{ opacity: 1, x: 0 }} transition={{ duration: 0.6, delay: 0.2 }} viewport={{ once: true, amount: 0.3 }}>
            <div className="relative">
              <div className="absolute -top-12 -right-12 w-64 h-64 bg-secondary/10 rounded-full blur-3xl"></div>
              <div className="absolute -bottom-12 -left-12 w-64 h-64 bg-primary/10 rounded-full blur-3xl"></div>
              <div className="relative glass-card p-xl rounded-xxl border border-slate-200 shadow-xl overflow-hidden">
                <h4 className="font-headline-sm text-headline-sm mb-lg text-primary">The Heutrix Method</h4>
                <ul className="space-y-md">
                  <li className="flex items-center gap-md">
                    <div className="w-8 h-8 rounded-full bg-secondary-container flex items-center justify-center text-on-secondary-container">1</div>
                    <p className="font-body-md text-body-md">Diagnostic: Finding the workflow gaps</p>
                  </li>
                  <li className="flex items-center gap-md">
                    <div className="w-8 h-8 rounded-full bg-secondary-container flex items-center justify-center text-on-secondary-container">2</div>
                    <p className="font-body-md text-body-md">Process: Uncovering manual clicks</p>
                  </li>
                  <li className="flex items-center gap-md">
                    <div className="w-8 h-8 rounded-full bg-secondary-container flex items-center justify-center text-on-secondary-container">3</div>
                    <p className="font-body-md text-body-md">Automation: Reducing repeated admin</p>
                  </li>
                  <li className="flex items-center gap-md">
                    <div className="w-8 h-8 rounded-full bg-secondary-container flex items-center justify-center text-on-secondary-container">4</div>
                    <p className="font-body-md text-body-md">Safe AI: Scaling with patient trust</p>
                  </li>
                </ul>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
"""

components['FAQ.jsx'] = """import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

export default function FAQ() {
  const [openIndex, setOpenIndex] = useState(null);

  const faqs = [
    { q: 'What does Heutrix Labs do?', a: 'Heutrix Labs helps health practices improve operational workflows through practical process improvement, automation, better visibility, safe AI support and lightweight internal systems.' },
    { q: 'Who does Heutrix Labs work with?', a: 'We work primarily with allied health, dental, medical, specialist and care-related practices that need clearer workflows, better follow-up, safer AI use or better visibility over day-to-day operations.' },
    { q: 'What is the Workflow Diagnostic?', a: 'It is a paid assessment that helps identify the best workflow to improve first. It is designed for practices that know something is taking too much time, creating avoidable risk or causing inconsistent follow-up, but are not sure what should be changed first.' },
    { q: 'Can we use AI with patient or client information?', a: 'Not without a careful review. Heutrix Labs does not recommend entering identifiable patient, client, participant, staff or sensitive business information into publicly available generative AI tools.' },
    { q: 'Do you guarantee cost savings or productivity improvements?', a: 'No. Heutrix Labs does not guarantee cost savings, revenue growth, productivity gains or business performance improvements. Outcomes depend on implementation, adoption, data quality, staff use and management oversight.' }
  ];

  return (
    <section className="py-xxl px-lg bg-surface" id="faq">
      <div className="max-w-3xl mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true }} className="text-center mb-xxl">
          <h2 className="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-md">Operational Clarity</h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant">Common questions about working with Heutrix Labs.</p>
        </motion.div>
        
        <div className="space-y-md">
          {faqs.map((faq, index) => (
            <motion.div 
              initial={{ opacity: 0, y: 20 }} 
              whileInView={{ opacity: 1, y: 0 }} 
              transition={{ duration: 0.4, delay: index * 0.1 }} 
              viewport={{ once: true }}
              key={index} 
              className={`border border-slate-200 rounded-xl overflow-hidden bg-white transition-all ${openIndex === index ? 'shadow-md border-secondary/30' : 'shadow-sm'}`}
            >
              <button 
                className="w-full flex items-center justify-between p-lg text-left hover:bg-slate-50 transition-colors" 
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
              >
                <span className="font-headline-sm text-headline-sm text-primary">{faq.q}</span>
                <motion.span 
                  animate={{ rotate: openIndex === index ? 180 : 0 }} 
                  className="material-symbols-outlined" 
                  data-icon="expand_more"
                >
                  expand_more
                </motion.span>
              </button>
              <AnimatePresence>
                {openIndex === index && (
                  <motion.div 
                    initial={{ height: 0, opacity: 0 }} 
                    animate={{ height: 'auto', opacity: 1 }} 
                    exit={{ height: 0, opacity: 0 }} 
                    transition={{ duration: 0.3 }}
                    className="px-lg pb-lg text-on-surface-variant font-body-md overflow-hidden"
                  >
                    {faq.a}
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
"""

components['Contact.jsx'] = """import React from 'react';
import { motion } from 'framer-motion';

export default function Contact() {
  return (
    <section className="py-xxl px-lg bg-surface" id="contact">
      <div className="max-w-container-max mx-auto">
        <div className="grid lg:grid-cols-2 gap-xxl">
          <motion.div initial={{ opacity: 0, x: -30 }} whileInView={{ opacity: 1, x: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.3 }}>
            <h2 className="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-md">Book a free fit call.</h2>
            <p className="font-body-lg text-body-lg text-on-surface-variant mb-lg">We will discuss the workflow or operational issue, what is currently difficult to manage and whether Heutrix Labs is the right fit to help. The purpose of this call is to decide the best next step.</p>
            <div className="p-md bg-secondary-container/30 border border-secondary/20 rounded-xl mb-xl">
              <p className="font-label-md text-label-md text-primary mb-xs">Privacy Note Before Submitting</p>
              <p className="font-body-sm text-body-sm text-on-surface-variant">Please do not include patient names, Medicare numbers, clinical details, diagnosis information, participant records, or other sensitive information in this form. A general description of the workflow is enough for the fit call.</p>
            </div>
            <div className="space-y-lg">
              <div className="flex items-center gap-lg">
                <div className="w-12 h-12 rounded-full bg-surface-container flex items-center justify-center text-primary">
                  <span className="material-symbols-outlined" data-icon="mail">mail</span>
                </div>
                <div>
                  <p className="font-label-md text-label-md text-primary">Email Us</p>
                  <p className="font-body-md text-body-md text-on-surface-variant">hello@heutrixlabs.com</p>
                </div>
              </div>
            </div>
          </motion.div>
          
          <motion.div initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.2 }} viewport={{ once: true, amount: 0.3 }}>
            <form className="glass-card p-xl rounded-xxl border border-slate-200 shadow-xl space-y-md" onSubmit={(e) => e.preventDefault()}>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-md">
                <div className="flex flex-col gap-xs">
                  <label className="font-label-md text-label-md text-primary px-xs">Name</label>
                  <input className="p-md rounded-lg border border-slate-300 focus:ring-2 focus:ring-secondary/50 outline-none" placeholder="John Doe" type="text"/>
                </div>
                <div className="flex flex-col gap-xs">
                  <label className="font-label-md text-label-md text-primary px-xs">Practice / Organisation Name</label>
                  <input className="p-md rounded-lg border border-slate-300 focus:ring-2 focus:ring-secondary/50 outline-none" placeholder="City Dental" type="text"/>
                </div>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-md">
                <div className="flex flex-col gap-xs">
                  <label className="font-label-md text-label-md text-primary px-xs">Email Address</label>
                  <input className="p-md rounded-lg border border-slate-300 focus:ring-2 focus:ring-secondary/50 outline-none" placeholder="john@example.com" type="email"/>
                </div>
                <div className="flex flex-col gap-xs">
                  <label className="font-label-md text-label-md text-primary px-xs">Practice Type</label>
                  <input className="p-md rounded-lg border border-slate-300 focus:ring-2 focus:ring-secondary/50 outline-none" placeholder="Allied Health, Dental, etc." type="text"/>
                </div>
              </div>
              <div className="flex flex-col gap-xs">
                <label className="font-label-md text-label-md text-primary px-xs">Operational Status</label>
                <div className="space-y-sm mt-xs">
                  <label className="flex items-center gap-md p-md border border-slate-200 rounded-lg cursor-pointer hover:bg-slate-50">
                    <input className="w-5 h-5 text-secondary rounded" type="checkbox"/>
                    <span className="font-body-sm">Are patient, client, participant, staff or sensitive records involved?</span>
                  </label>
                  <label className="flex items-center gap-md p-md border border-slate-200 rounded-lg cursor-pointer hover:bg-slate-50">
                    <input className="w-5 h-5 text-secondary rounded" type="checkbox"/>
                    <span className="font-body-sm">Are staff currently using AI tools at work?</span>
                  </label>
                  <label className="flex items-center gap-md p-md bg-error-container/20 border border-error/20 rounded-lg cursor-pointer hover:bg-error-container/30">
                    <input className="w-5 h-5 text-error rounded" type="checkbox" required/>
                    <span className="font-body-sm font-bold text-on-surface">I confirm I have NOT included identifiable patient, clinical or sensitive information in this form.</span>
                  </label>
                </div>
              </div>
              <button className="w-full bg-primary text-on-primary py-lg rounded-xl font-headline-sm hover:opacity-95 transition-all shadow-md mt-md">
                Request Fit Call
              </button>
            </form>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
"""

components['Footer.jsx'] = """import React from 'react';

export default function Footer() {
  return (
    <footer className="bg-primary text-on-primary pt-xxl pb-xl px-lg border-t border-on-primary-fixed-variant">
      <div className="max-w-container-max mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-start gap-lg mb-xxl">
          <div className="max-w-md">
            <span className="font-headline-sm text-headline-sm text-secondary-fixed font-bold block mb-md">Heutrix Labs</span>
            <p className="font-body-sm text-body-sm text-on-primary-fixed-variant mb-md">
              Heutrix Labs helps Australian health practices improve operational workflows through practical process improvement, automation, safe AI support, better visibility and maintainable systems.
            </p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-xl">
            <div>
              <p className="font-label-md text-label-md text-white mb-md">Company</p>
              <ul className="space-y-sm font-body-sm text-on-primary-fixed-variant">
                <li><a className="hover:text-white transition-colors" href="#about">About</a></li>
                <li><a className="hover:text-white transition-colors" href="#services">Services</a></li>
                <li><a className="hover:text-white transition-colors" href="#faq">FAQ</a></li>
              </ul>
            </div>
            <div>
              <p className="font-label-md text-label-md text-white mb-md">Legal</p>
              <ul className="space-y-sm font-body-sm text-on-primary-fixed-variant">
                <li><a className="hover:text-white transition-colors" href="#">Privacy Policy</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Terms of Use</a></li>
                <li><a className="hover:text-white transition-colors" href="#">Website Disclaimer</a></li>
              </ul>
            </div>
            <div className="col-span-2 md:col-span-1">
              <p className="font-label-md text-label-md text-white mb-md">Social</p>
              <div className="flex gap-md">
                <a className="w-10 h-10 rounded-full bg-on-primary-fixed-variant/20 flex items-center justify-center hover:bg-secondary-fixed hover:text-on-secondary-fixed transition-all" href="#">
                  <span className="material-symbols-outlined text-[20px]" data-icon="share">share</span>
                </a>
              </div>
            </div>
          </div>
        </div>
        <div className="border-t border-on-primary-fixed-variant pt-lg flex flex-col gap-lg">
          <div className="p-lg bg-on-primary-fixed-variant/10 rounded-xl">
            <p className="font-label-sm text-label-sm font-bold text-secondary-fixed mb-xs uppercase tracking-widest">Website Disclaimer</p>
            <p className="font-body-sm text-body-sm text-on-primary-fixed-variant">
              Heutrix Labs provides workflow improvement, safe AI support, practice visibility builds and operational systems support. Heutrix Labs does not provide legal advice, financial advice, tax advice, employment advice, clinical advice, medical advice, regulatory advice, official audit services, NDIS registration readiness, audit readiness, evidence preparation, mock audit support, compliance gap assessments or assurance services.
            </p>
          </div>
          <div className="flex flex-col md:flex-row justify-between items-center gap-md">
            <p className="font-body-sm text-body-sm text-on-primary-fixed-variant">© 2024 Heutrix Labs. All rights reserved.</p>
          </div>
        </div>
      </div>
    </footer>
  );
}
"""

for name, content in components.items():
    with open(f'src/components/{name}', 'w') as f:
        f.write(content)

