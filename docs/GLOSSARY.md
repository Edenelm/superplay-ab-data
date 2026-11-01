# Glossary (org terms)

Generated 2026-11-01T13:31:33+02:00 from local sources. {'concepts': 58, 'unclear': 31, 'inferred_from_usage': 19, 'defined_in_source': 8}. Canonical names are the org's own terms. `unclear` = needs an answer from the team.

| Term | Status | Definition (he) | Games (tests) | Not the same as | Open question |
|---|---|---|---|---|---|
| FTD | inferred_from_usage | רכישה ראשונה של שחקן; גם שם ההצעה שמוצגת לפני רכישה ראשונה (FTD offer). | DICE:4, DOM:11, DIS:4 | FTD Rate (מדד המרה בלשוניות התוצאות) הוא שיעור, לא אוכלוסייה.; FTUE היא חוויית משתמש חדש, לא רכישה. | לאשר: FTD = First Time Deposit (רכישה ראשונה)? |
| STD | unclear | — | DICE:0, DOM:1, DIS:2 | — | STD = Second Time Deposit (רכישה שנייה)? האם אותה משמעות ב-Dice, Domino ו-Disney? |
| FTUE | inferred_from_usage | חוויית המשתמש בשלבים הראשונים (מופיע בסוגריים בשמות טסטים, למשל 'Move quest from level 32 to 200 (FTUE)'). | DICE:2, DOM:8 | FTUE מול FTD: בטסט 8 Box ב-Domino השם אומר FTUE וה-WhatsApp אומר FTD. | מה טווח ה-FTUE בכל משחק (עד איזה Level/Kingdom)? |
| PU | inferred_from_usage | משתמשים משלמים (Paying Users); מצוטט כמדד בתוצאות ('PU +0.5%'). | DICE:2 | PAU הוא מדד נפרד שמצוטט לצד PU. | האם PU זהה ל-payers בהגדרת data/metric_definitions.json (DICE.payers וכו')? |
| NPU | inferred_from_usage | משתמשים שלא שילמו (Non-Paying Users). | DOM:1, DIS:5 | — | האם 'לא-משלמים' זה 'אף פעם לא שילמו' או 'לא שילמו בחלון מסוים'? |
| PAU | unclear | — | DICE:0 | לא זהה ל-PU (מצוטטים יחד עם ערכים שונים). | מה ההגדרה של PAU (Paying Active Users?) ומה ההבדל מ-PU? |
| DAU | defined_in_source | Daily Active Users. ההגדרה לכל משחק נמצאת ב-data/metric_definitions.json (DICE.active_users_dau, DIS.active_users_dau; ב-Domino אין מקור, null). | DICE:1 | ההגדרה הטכנית שונה בין המשחקים (טבלאות שונות); ראו METRIC_DEFINITIONS.md. | — |
| ARPPU | inferred_from_usage | הכנסה ממוצעת למשתמש משלם (Average Revenue Per Paying User). | DICE:0, DIS:0 | ARPDAU מחושב לפי DAU, לא לפי משלמים. | האם ARPPU מחושב על Gross או Net? |
| ARPDAU | inferred_from_usage | הכנסה ממוצעת למשתמש פעיל יומי. | DICE:0 | — | ARPDU ו-ARPDAU הם אותו מדד? |
| Revenue | defined_in_source | ההגדרות של Gross, Net ו-ad revenue לכל משחק נמצאות ב-data/metric_definitions.json. בתוצאות טסטים 'Revenue' הוא כפי שמופיע בלשונית התוצאות. | DICE:4, DOM:5, DIS:1 | Gross אינו בר השוואה בין המשחקים (ALL.gross_comparability). | האם 'Revenue' בלשוניות התוצאות כולל פרסומות? (needs_approval ב-METRIC_DEFINITIONS.md) |
| VIP | unclear | — | DICE:3, DOM:3 | ב-Dice, VIP מופיע כסגמנט יעד; ב-Domino מופיעים רכיבי תוכנית VIP. אל תניחו אותה הגדרה. | מה סף ה-VIP בכל משחק? האם ב-Domino זו תוכנית (onboarding/frame) ולא רק סגמנט? |
| Dormants | unclear | — | DICE:9, DOM:2, DIS:6 | Churn/churners מופיע כמונח נפרד; לא ידוע אם הספים זהים. | כמה ימי אי-פעילות מגדירים Dormant בכל משחק? מה זה 'dormant 3' ב-Domino? |
| Churners | unclear | — | DICE:6, DOM:5, DIS:1 | Dormants (ראו למעלה). | האם churn = 7 ימי אי-פעילות בכל המשחקים, או רק בטסט של Domino? |
| CZ | unclear | — | DICE:12, DOM:3, DIS:11 | השימוש שונה: ב-Dice כיחידת ערך להצעה, ב-Domino כבסיס לסגמנטציה של החנות. לא לאחד עד שיאושר. | מה המשמעות של CZ? האם זה אותו מנגנון בשלושת המשחקים (ערך/מחיר מותאם לשחקן)? |
| PB | unclear | — | DICE:16, DOM:4, DIS:7 | ב-Dice ל-PB יש 'Points' ו-PPR; ב-Domino יש לו 'free entry'. ייתכן שאלה פיצ'רים שונים עם אותו קיצור. | מה זה PB בכל משחק? האם אותו פיצ'ר? |
| RV | inferred_from_usage | Rewarded Video. ב-Dice יש 'סגמנט RV לא-משלמים', ומשתמש שרוכש יוצא ממנו לתקופה (14 יום בקונטרול של 1110). | DICE:12, DOM:3, DIS:2 | Domino 'RV Mania' ו-Disney 'RV 8box' הם פיצ'רים שונים שמבוססים על RV; הסגמנט של Dice לא בהכרח קיים בהם. | לאשר: RV = Rewarded Video? |
| DTC | defined_in_source | רכישה ב-web (DTC/Stripe) במקום ב-store. | DICE:9, DOM:4, DIS:2 | — | — |
| Scare Screen | inferred_from_usage | מסך אזהרה לפני רכישת DTC (Domino 1494: 'Google warning'). | DICE:2, DOM:1 | — | האם זה אותו מסך ב-Dice (1103) וב-Domino (1494)? |
| DDJ | unclear | — | DICE:3 | — | מה זה DDJ (אירוע MTX ב-Dice)? |
| PT | unclear | — | DICE:2 | — | מה זה PT ב-Dice? |
| MTX | inferred_from_usage | צוות ופיצ'רי ה-live-ops (אירועים ומבצעים). 'Test scheduled ... on MTX side' (Domino). | DICE:2, DOM:1, DIS:6 | — | לאשר את ההגדרה. |
| K (Kingdom) | defined_in_source | Dice: מספר Kingdom (התקדמות). 'X2 Ticks Per Hour K199 and under' = 'עבור קינגדום 1 עד 199'. | DICE:12 | ב-Domino ו-Disney ההתקדמות נמדדת ב-Level, לא ב-K. | — |
| AD (Active Days) | defined_in_source | Active Days. הפריט '1106 - Remove AD from Segmentation' והדשבורד '1106 - Remove Active Days from Segmentation' מתייחסים לאותו טסט. | DICE:5 | 'RPS AD ECHAD' הוא כנראה צירוף אחר (ECHAD = 'אחד'?), לא בהכרח Active Days. | — |
| Level | inferred_from_usage | שלב/רמה (Domino ו-Disney). | DICE:1, DOM:10, DIS:16 | ב-Dice ההתקדמות היא K (Kingdom). | — |
| 3PO | defined_in_source | הצעה עם שלוש נקודות מחיר (למשל FTD 3PO $3/$5/$7). | DICE:1, DOM:0 | — | — |
| 8 Box | unclear | — | DOM:2, DIS:4 | 6Box (Disney/Dice) הוא פורמט אחר. | מה המבנה של 8 Box (8 קופסאות/שלבים)? האם זהה ב-Domino וב-Disney? |
| Starter Pack | inferred_from_usage | הצעת פתיחה לשחקנים חדשים. ב-Domino היא חלק מ-FTD offer. | DICE:1, DOM:1, DIS:3 | — | — |
| Dream Pass | inferred_from_usage | Pass עם משימות ותגמולים, ויש לו גרסת Premium בתשלום ('encourage players to buy the Premium Pass'). | DICE:9, DOM:4 | — | DP ב-Domino ('Remove DP pop up ... OOC') הוא אותו Dream Pass? |
| Trail | unclear | — | DICE:23, DOM:4, DIS:1 | מבנה ה-Trail ב-Dice (tiers, wheel, GP) לא ידוע ב-Domino וב-Disney. | האם Trail הוא אותו סוג אירוע בשלושת המשחקים? |
| Recompletion | inferred_from_usage | השלמה חוזרת של אירוע (למשל Trail) אחרי ההשלמה הראשונה. | DICE:5, DOM:1 | — | — |
| GP | unclear | — | DICE:6, DIS:3 | — | GP = Grand Prize? האם זהה ב-Dice וב-Disney? |
| ATW | unclear | — | DICE:3 | — | ATW = Along The Way (תגמולי ביניים)? |
| DR | unclear | — | DICE:9, DIS:4 | DRC ב-Disney הוא מונח אחר, לא להניח קשר. | מה זה DR ב-Dice? |
| DRC | unclear | — | DIS:3 | DR ב-Dice. | מה זה DRC ב-Disney? |
| TE | unclear | — | DICE:2 | — | מה זה TE ב-Dice? |
| Rolls / Ticks | defined_in_source | Dice: רולים חינמיים שמתקבלים לפי טיימר. 'X2 Ticks Per Hour' מקצר את הטיימר משעה לחצי שעה, עם אותה כמות רולים בכל איטרציה. | DICE:27, DIS:1 | — | — |
| Max Bet | defined_in_source | Dice: ערך ברירת המחדל של ההימור המקסימלי (100 מעל K110+ לפני הטסט 1105). | DICE:1 | — | — |
| Duel | inferred_from_usage | אירוע של דו-קרבות מול בוטים ('Duel event 1: 4 Duels 5/15/15/15', Dice). | DICE:7, DOM:3, DIS:5 | Duel ב-Domino (1501 Duel vs Tournament Onboarding) וב-Disney (Duel Economy) לא בהכרח באותו מבנה. | מה המשמעות של 5/15/15/15? |
| Tournament | inferred_from_usage | אירוע טורניר. ב-Dice עוברים ל-Tournament V2 ובודקים שמשחזר את הישן. | DICE:14, DOM:2, DIS:1 | — | — |
| Weekly Goals | unclear | — | DICE:8, DOM:4 | — | האם Weekly Goals (Dice) ו-Weekly tasks (Domino) הם אותו פיצ'ר? |
| Genie | unclear | — | DOM:1 | — | מה זה Genie ב-Domino ומה זה 'agenda' שלו? |
| Whammy | unclear | — | DICE:2 | — | מה זה Whammy, ומה זה DT finishers? |
| Piggy | unclear | — | DICE:2 | — | Piggy Bank? האם קשור ל-PB? |
| Pity | unclear | — | DICE:3, DOM:8, DIS:19 | — | מה מנגנון ה-Pity בכל משחק? |
| FU | unclear | — | DICE:4, DOM:2, DIS:4 | — | מה זה FU? האם אותה משמעות בכל משחק? |
| WR | unclear | — | DOM:1, DIS:5 | — | WR = Win Rate? האם זהה ב-Disney וב-Domino? |
| ES | unclear | — | DOM:1, DIS:6 | — | ES = Extra Stock? האם אותו דבר ב-Disney? |
| OOC / OOR | inferred_from_usage | מצב שבו השחקן נגמר לו משאב (Out Of Coins / Out Of Rolls); טריגר להצעה או לפופאפ. | DICE:6, DOM:1, DIS:3 | — | לאשר את ההרחבה (OOR = Out of Rolls?). |
| Low balance | unclear | — | DICE:1, DOM:2, DIS:1 | — | מה סף ה-low balance? |
| DSLP / DFI | unclear | — | DIS:9 | — | DSLP = Days Since Last Purchase? DFI = Days From Install? |
| Segment split notation | unclear | — | DICE:1 | ABTestV2 (Dice) ו-fn_ABTest (Domino) הן פונקציות שונות. | מה המשמעות של כל פרמטר (מודולו, טווח, salt, דגל)? האם החלוקה ל-50/50 או לשליש נכונה? |
| Phase | inferred_from_usage | שלב בהרצה של אותו טסט (למשל שינוי גודל הטסט 10%→20%/30%). | DICE:6 | — | — |
| Braze | inferred_from_usage | כלי שליחת push/הודעות ('VIP Braze Push'). | DICE:1 | — | — |
| Push | inferred_from_usage | הודעת push לשחקן. | DICE:3, DIS:2 | 'push hard to FU' (Dice) זה ביטוי, לא push notification. | — |
| AYS | unclear | — | DIS:1 | — | מה זה AYS offer? |
| CC | unclear | — | DIS:1 | CC ב-Disney (Level List) מול 'cc abilities' ב-Domino. | מה זה CC בכל הקשר? (ב-Disney זו כנראה רשימת levels; ב-Domino 'cc abilities' כנראה משהו אחר) |
| GT | unclear | — | DICE:1 | — | מה זה GT? |
| BWF | unclear | — | DICE:6 | — | מה זה BWF? |
