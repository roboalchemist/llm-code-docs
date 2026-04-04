# Source: https://docs.replit.com/additional-resources/cheat-sheet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Replit Cheat Sheet

> A handy cheat sheet summarizing the key features and functionalities of Replit.

export const AuthorCard = ({img = "https://replit.com/cdn-cgi/image/width=256,quality=80,format=auto/https://storage.googleapis.com/replit/images/1730840970400_e885f16578bbbb227adbfeb7b979be34.jpeg", href = "https://youtube.com/@mattpalmer", name = "Matt Palmer", role = "Head of Developer Relations"}) => {
  return <a href={href} target="_blank" className="card block not-prose font-normal group relative my-2 ring-2 ring-transparent rounded-xl border border-gray-100 shadow-md dark:shadow-none shadow-gray-300/10 dark:border-gray-800/50 overflow-hidden cursor-pointer hover:!border-primary dark:hover:!border-primary-light">
      <div className="flex items-center gap-2 p-4">
        <div className="flex-shrink-0">
          <img src={img} alt={name} className="w-12 h-12 rounded-full object-cover" />
        </div>
        <div className="flex-grow">
          <h3 className="text-base font-semibold mb-0.5 text-inherit">{name}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400 m-0">{role}</p>
        </div>
      </div>
    </a>;
};

<AuthorCard />

Here's a handy cheat sheet summarizing the key features and functionalities of Replit. Keep it nearby for quick reference!

<Frame>
  <img src="https://mintcdn.com/replit/-6g2hQCrMskerX65/images/additional-resources/replit-cheat-sheet-1.png?fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=d4bf98b65e1ccbd1ded3a2d75d40fd11" alt="Replit Cheat Sheet" data-og-width="3216" width="3216" data-og-height="1874" height="1874" data-path="images/additional-resources/replit-cheat-sheet-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/-6g2hQCrMskerX65/images/additional-resources/replit-cheat-sheet-1.png?w=280&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=6b059d93d583553206e248646d438efc 280w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/additional-resources/replit-cheat-sheet-1.png?w=560&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=95b63017a188db791cf1178add88f254 560w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/additional-resources/replit-cheat-sheet-1.png?w=840&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=1da7268ca1df87914c938d14e2f760c8 840w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/additional-resources/replit-cheat-sheet-1.png?w=1100&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=a4f8d8652706fbb66307fbbe0349d676 1100w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/additional-resources/replit-cheat-sheet-1.png?w=1650&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=40756e0de6e963b485a3e0f0d8156aae 1650w, https://mintcdn.com/replit/-6g2hQCrMskerX65/images/additional-resources/replit-cheat-sheet-1.png?w=2500&fit=max&auto=format&n=-6g2hQCrMskerX65&q=85&s=d4a266f330d1782618ce6e2d6cb606e8 2500w" />
</Frame>
