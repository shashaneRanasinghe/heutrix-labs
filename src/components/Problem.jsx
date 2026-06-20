import React from 'react';
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
    <section className="py-xxl px-lg bg-primary text-on-primary relative z-20" id="problem">
      <div className="max-w-container-max mx-auto">
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="max-w-4xl mb-xxl">
          <h2 className="font-headline-md text-headline-md text-white mb-md drop-shadow-lg">When important work is spread across memory, inboxes and spreadsheets, even capable teams can lose visibility.</h2>
          <p className="font-body-lg text-body-lg text-on-primary-fixed-variant">
            Many practice teams are highly capable, but the systems around them have not always kept up with growth, staff changes, patient demand or disconnected tools. Heutrix Labs helps identify where important admin and operational work needs clearer ownership, tracking, reminders, handover or review.
          </p>
        </motion.div>

        <h3 className="font-headline-md text-headline-md text-secondary-fixed mb-xl">You may notice:</h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-lg">
          {issues.map((issue, i) => (
            <motion.div 
              key={i} 
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: (i % 2) * 0.1 }}
              viewport={{ once: true, amount: 0.2 }}
              className="bg-white/5 backdrop-blur-xl rounded-xl p-lg border border-white/10 flex items-start gap-md hover:bg-white/10 transition-colors"
            >
              <div className="w-10 h-10 rounded-full bg-secondary-fixed/20 text-secondary-fixed flex items-center justify-center shrink-0">
                <span className="material-symbols-outlined text-[20px]">adjust</span>
              </div>
              <p className="font-headline-sm text-headline-sm text-white pt-1">{issue}</p>
            </motion.div>
          ))}
        </div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} viewport={{ once: true, amount: 0.2 }} className="mt-xxl max-w-4xl">
          <p className="font-body-lg text-body-lg text-white font-medium border-l-4 border-secondary pl-lg">
            Heutrix Labs helps turn these pressure points into clearer workflows, practical tracking systems, safer AI practices and better visibility for day-to-day decisions.
          </p>
        </motion.div>
      </div>
    </section>
  );
}
