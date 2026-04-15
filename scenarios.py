SCENARIOS = [
    {
        "id": 1, 
        "label": "Post-Interview Follow-up",
        "intent": "Follow up after a job interview",
        "facts": [
            "Interview with Sarah Chen and Mark Davis on Tuesday at 2PM", 
            "Applied for Senior Product Manager at TechCorp", 
            "Discussed Q4 roadmap strategy and cross-functional team leadership", 
            "Can start within 4 weeks notice period"
        ],
        "tone": "professional and warmly grateful",
        "referenceEmail": "Subject: Thank You – Senior PM Interview...\n\nDear Sarah and Mark,\n..."
    },
    {
        "id": 2, "label": "Deadline Extension Request",
        "intent": "Request a project deadline extension from manager",
        "facts": ["Project: Annual Marketing Report", "Original deadline: Friday, April 18", "Requesting extension to Wednesday, April 23", "Delay caused by unexpected data pipeline failure on April 12", "Quality of deliverable will not be compromised"],
        "tone": "professional, apologetic, and solution-focused",
        "referenceEmail": "Subject: Extension Request – Annual Marketing Report\n\nHi [Manager],\n\nI wanted to flag a timeline concern for the Annual Marketing Report due Friday. On April 12, an unexpected data pipeline failure disrupted our source data, which I am actively resolving.\n\nI respectfully request a five-day extension to Wednesday, April 23 to ensure the deliverable meets our quality standards. I will keep you updated on progress throughout.\n\nThank you for your understanding.\n\nBest,\n[Name]"        
  },
    {
        "id": 3, "label": "Client Proposal Follow-up",
        "intent": "Follow up on a submitted proposal with a prospect",
        "facts": ["Proposal submitted two weeks ago for a $120K enterprise software contract", "Client: Meridian Logistics, contact is VP Operations James Whitfield", "Proposal includes 90-day implementation timeline", "Offer to arrange a 30-minute Q&A call this week"],
        "tone": "confident, professional, and gently urgent",
        "referenceEmail": "Subject: Following Up – Enterprise Proposal for Meridian Logistics\n\nDear James,\n\nTwo weeks have passed since we submitted our enterprise software proposal, and I wanted to touch base.\n\nOur $120K package includes a 90-day implementation timeline designed around Meridian's operational cadence. I would love to arrange a 30-minute call this week to walk through any questions and ensure alignment before you make your decision.\n\nWould Thursday or Friday work for you?\n\nBest regards,\n[Name]"        
  },
    {
        "id": 4, "label": "Team Offsite Announcement",
        "intent": "Announce a team offsite event to direct reports",
        "facts": ["Team offsite on May 9-10 in Coorg, Karnataka", "Agenda: Q2 retrospective, team-building activities, strategy workshop", "All travel and accommodation covered by the company", "RSVP required by April 25"],
        "tone": "enthusiastic, casual, and inclusive",
        "referenceEmail": "Subject: We're Heading to Coorg! Team Offsite – May 9-10\n\nHey team!\n\nExciting news — we are doing a two-day offsite in Coorg on May 9-10! The agenda covers our Q2 retrospective, a strategy workshop, and (most importantly) some proper team time away from screens.\n\nAll travel and accommodation is sorted by the company. Just drop me your RSVP by April 25 so I can finalise logistics.\n\nCan't wait — it's going to be a great couple of days.\n\n[Manager Name]"
  },
    {
        "id": 5, "label": "Customer Complaint Resolution",
        "intent": "Respond to a customer complaint about a delayed order",
        "facts": ["Customer: Priya Sharma, Order #ORD-48291", "Package delayed 8 days due to a courier network outage", "Full refund of shipping fee has been processed", "10% discount voucher added to account for next purchase", "Estimated delivery now April 17"],
        "tone": "empathetic, apologetic, and reassuring",
        "referenceEmail": "Subject: We're Sorry, Priya – Update on Order #ORD-48291\n\nDear Priya,\n\nI sincerely apologise for the frustrating delay with your order. A courier network outage caused an 8-day disruption that fell well short of the experience we want to provide.\n\nI have processed a full refund of your shipping fee and added a 10% discount voucher to your account for your next purchase. Your order is now estimated to arrive on April 17.\n\nThank you for your patience, and please do not hesitate to reach out if I can help further.\n\nWarm regards,\nCustomer Care Team"
  },
    {
        "id": 6, "label": "Partnership Proposal",
        "intent": "Propose a strategic partnership to a potential partner company",
        "facts": ["Our company: Nexus Analytics (data intelligence platform)", "Potential partner: Orbit Retail (India's 3rd-largest e-commerce platform)", "Proposed integration: real-time inventory analytics", "Projected 23% reduction in overstock costs for Orbit", "Request a 20-minute intro call with their BD team"],
        "tone": "formal, confident, and value-focused",
        "referenceEmail": "Subject: Strategic Partnership Proposal – Nexus Analytics × Orbit Retail\n\nDear [BD Lead],\n\nNexus Analytics is reaching out to explore a strategic data partnership with Orbit Retail.\n\nOur real-time inventory analytics platform has helped e-commerce clients reduce overstock costs by an average of 23%. We believe a deep integration with Orbit's systems could deliver significant efficiency gains as you scale.\n\nI would welcome a 20-minute call with your business development team to discuss how we might structure this collaboration. Would early next week suit you?\n\nRespectfully,\n[Name], Nexus Analytics"
  },
    {
        "id": 7, "label": "Product Launch Announcement",
        "intent": "Announce a new product launch to existing customers",
        "facts": ["New product: FlowDesk Pro 3.0 — AI-powered project management tool", "Key features: automated task prioritisation, Slack/Jira integration, real-time team analytics", "Launch date: May 1", "Existing customers get 30% early-access discount valid until April 30", "Free 14-day trial available"],
        "tone": "enthusiastic, exciting, and customer-focused",
        "referenceEmail": "Subject: Introducing FlowDesk Pro 3.0 — Built for Teams Like Yours\n\nHi [Name],\n\nBig news: FlowDesk Pro 3.0 launches on May 1 — and as a valued customer, you get first access.\n\nThe new version features AI-powered task prioritisation, native Slack and Jira integration, and real-time team analytics that cut planning time in half. We think you will love it.\n\nTo say thank you for your loyalty, use code EARLYBIRD at checkout for 30% off — valid until April 30. Or start your free 14-day trial today, no credit card needed.\n\n[CTA Button]\n\nExcited to hear what you think!\nThe FlowDesk Team"
  },
    {
        "id": 8, "label": "Reference Letter Request",
        "intent": "Request a professional reference letter from a former manager",
        "facts": ["Applying for Data Science Lead role at Stripe", "Worked under Dr. Arjun Mehta at DataBridge Solutions for 3 years", "Key achievements: led ML pipeline reducing fraud detection errors by 40%, mentored a team of 5 analysts", "Application deadline: April 28", "Reference needed by April 25 for submission"],
        "tone": "polite, humble, and appreciative",
        "referenceEmail": "Subject: Reference Request – Data Science Lead Application (Stripe)\n\nDear Dr. Mehta,\n\nI hope you are well. I am reaching out to ask whether you would be willing to write a reference letter on my behalf.\n\nI am applying for a Data Science Lead role at Stripe, and given the three years I spent under your mentorship at DataBridge — particularly the ML pipeline project that reduced fraud errors by 40% — I believe your perspective would carry great weight.\n\nThe deadline is April 28, so I would need the letter by April 25 if possible. I am happy to send a summary of the role and key themes if that would help.\n\nThank you so much for considering this request.\n\nWarmly,\n[Name]"
  },
    {
        "id": 9, "label": "Vendor Price Negotiation",
        "intent": "Negotiate better pricing terms with a software vendor",
        "facts": ["Vendor: CloudServe Inc., account manager Rachel Torres", "Current contract: $18,000/year for cloud infrastructure", "Requesting 20% reduction to $14,400 based on 3-year commitment", "Benchmark: comparable services (AWS, GCP) offer equivalent specs for ~$13,500", "Open to multi-year lock-in or reduced SLA in exchange"],
        "tone": "assertive, data-driven, and professionally respectful",
        "referenceEmail": "Subject: Contract Renewal Discussion – Pricing Review\n\nDear Rachel,\n\nAs our current contract approaches renewal, I wanted to open a discussion on pricing before we commit to another term.\n\nOur benchmarking shows comparable infrastructure specifications on AWS and GCP at approximately $13,500 annually. To continue exclusively with CloudServe, we are proposing a revised rate of $14,400 (a 20% reduction) in exchange for a three-year commitment.\n\nWe value the relationship and are open to exploring adjusted SLA terms or other structures that work for both sides.\n\nWould you be available this week to discuss?\n\nBest,\n[Name]"
  },
    {
        "id": 10, "label": "Employee Recognition",
        "intent": "Recognise and celebrate an outstanding employee achievement",
        "facts": ["Employee: Kavya Reddy, Senior UX Designer", "Achievement: redesigned onboarding flow that improved user activation rate from 54% to 81%", "Project completed 2 weeks ahead of schedule with cross-team collaboration", "Bonus of ₹50,000 approved and will appear in next payroll cycle"],
        "tone": "warm, celebratory, and genuinely sincere",
        "referenceEmail": "Subject: Outstanding Work, Kavya — Thank You!\n\nHi Kavya,\n\nI wanted to take a moment to personally recognise the extraordinary work you delivered on the onboarding redesign project.\n\nMoving our user activation rate from 54% to 81% — and doing so two weeks ahead of schedule through seamless cross-team collaboration — is a remarkable achievement that will have lasting impact on our business.\n\nThe leadership team is truly grateful. A bonus of ₹50,000 has been approved and will appear in your next payroll cycle as a small acknowledgement of your exceptional contribution.\n\nThank you for the standard you set for all of us.\n\nWith appreciation,\n[Manager Name]"
  },
]

TONES = [
    "professional and formal", "warm and friendly", "empathetic and supportive",
    "confident and assertive", "casual and conversational", "enthusiastic and energetic",
    "apologetic and conciliatory", "urgent and direct", "data-driven and analytical"
]