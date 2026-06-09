import random

def main():
    alerts = get_alerts()
    random.shuffle(alerts)

    score = 0
    category_stats = {}

    print_banner()
    print("You are the night-shift SOC analyst.")
    print("Classify each alert based on its risk level.")
    print()

    for alert in alerts:
        initialize_category(category_stats, alert["category"])

        print_separator()
        print("ALERT:", alert["title"])
        print("Category:", alert["category"])
        print("Description:", alert["description"])
        print()
        print("Choose severity:")
        print("1. Benign")
        print("2. Suspicious")
        print("3. Critical")

        user_answer = get_user_severity()

        category_stats[alert["category"]]["total"] += 1

        if user_answer == alert["answer"]:
            print()
            print("Correct!")
            score += 1
            category_stats[alert["category"]]["correct"] += 1
        else:
            print()
            print("Incorrect.")
            print("Correct answer:", alert["answer"])

        print("Reason:", alert["reason"])
        print()

        input("Press Enter to continue...")
        print()

    print_report(score, len(alerts), category_stats)


def print_banner():
    print("====================================")
    print("      CYBER SENTINEL")
    print("      SOC ALERT TRAINER")
    print("====================================")
    print()


def print_separator():
    print("------------------------------------")


def get_user_severity():
    choice = input("Your answer: ")

    while choice != "1" and choice != "2" and choice != "3":
        print("Invalid option. Please enter 1, 2, or 3.")
        choice = input("Your answer: ")

    if choice == "1":
        return "Benign"
    elif choice == "2":
        return "Suspicious"
    else:
        return "Critical"


def initialize_category(category_stats, category):
    if category not in category_stats:
        category_stats[category] = {
            "correct": 0,
            "total": 0
        }


def print_report(score, total, category_stats):
    readiness_score = int((score / total) * 100)

    print("====================================")
    print("        SOC TRAINING REPORT")
    print("====================================")
    print("Total alerts reviewed:", total)
    print("Correct classifications:", score)
    print("SOC Readiness Score:", str(readiness_score) + "%")
    print("Rank:", get_rank(readiness_score))
    print()

    print("Category Performance:")
    for category in category_stats:
        correct = category_stats[category]["correct"]
        total_category = category_stats[category]["total"]
        print(category + ": " + str(correct) + "/" + str(total_category) + " correct")

    print()
    weakest_category = get_weakest_category(category_stats)
    strongest_category = get_strongest_category(category_stats)

    print("Strongest area:", strongest_category)
    print("Needs improvement:", weakest_category)
    print()

    print("Recommendation:")
    print(get_recommendation(weakest_category))
    print()
    print("Training complete. Stay sharp, analyst.")


def get_rank(readiness_score):
    if readiness_score == 100:
        return "Incident Commander"
    elif readiness_score >= 80:
        return "SOC Analyst"
    elif readiness_score >= 60:
        return "SOC Apprentice"
    else:
        return "SOC Intern"


def get_weakest_category(category_stats):
    weakest_category = ""
    weakest_score = 101

    for category in category_stats:
        correct = category_stats[category]["correct"]
        total = category_stats[category]["total"]
        percentage = (correct / total) * 100

        if percentage < weakest_score:
            weakest_score = percentage
            weakest_category = category

    return weakest_category


def get_strongest_category(category_stats):
    strongest_category = ""
    strongest_score = -1

    for category in category_stats:
        correct = category_stats[category]["correct"]
        total = category_stats[category]["total"]
        percentage = (correct / total) * 100

        if percentage > strongest_score:
            strongest_score = percentage
            strongest_category = category

    return strongest_category


def get_recommendation(category):
    if category == "Phishing":
        return "Review phishing indicators: suspicious domains, urgency, credential requests, and unusual sender behavior."
    elif category == "Brute Force":
        return "Review failed login patterns, account lockouts, source IP reputation, and successful login after many failures."
    elif category == "Malware":
        return "Review suspicious files, unexpected process execution, unusual network connections, and endpoint alerts."
    elif category == "Account Compromise":
        return "Review impossible travel, unusual login locations, MFA fatigue, and suspicious account behavior."
    elif category == "Data Loss":
        return "Review large file transfers, unusual downloads, cloud sharing, and sensitive data exposure."
    else:
        return "Review basic SOC triage: identify the asset, user, source, behavior, and business impact."


def get_alerts():
    return [
        {
            "title": "Multiple failed login attempts",
            "category": "Brute Force",
            "description": "The admin account received 25 failed login attempts from an external IP address.",
            "answer": "Suspicious",
            "reason": "Multiple failed logins against an admin account may indicate brute force activity."
        },
        {
            "title": "Successful login after many failures",
            "category": "Brute Force",
            "description": "A user had 18 failed login attempts followed by one successful login from the same IP.",
            "answer": "Critical",
            "reason": "A successful login after many failures may indicate that the attacker guessed the password."
        },
        {
            "title": "Normal password change",
            "category": "Account Compromise",
            "description": "A user changed their password from their usual device and usual location.",
            "answer": "Benign",
            "reason": "The activity matches normal user behavior and does not show suspicious indicators."
        },
        {
            "title": "Impossible travel login",
            "category": "Account Compromise",
            "description": "A user logged in from Peru and then 10 minutes later from Germany.",
            "answer": "Suspicious",
            "reason": "The same user cannot realistically travel between those countries in 10 minutes."
        },
        {
            "title": "Phishing link clicked",
            "category": "Phishing",
            "description": "A user clicked a suspicious email link and submitted their credentials.",
            "answer": "Critical",
            "reason": "Credential submission after clicking a suspicious link may lead to account compromise."
        },
        {
            "title": "Suspicious email detected",
            "category": "Phishing",
            "description": "An email claims the user's account will be suspended and asks them to verify credentials.",
            "answer": "Suspicious",
            "reason": "Urgency and credential requests are common phishing indicators."
        },
        {
            "title": "Newsletter received",
            "category": "Phishing",
            "description": "A user received a monthly newsletter from a known training platform they subscribed to.",
            "answer": "Benign",
            "reason": "The sender and content match expected behavior."
        },
        {
            "title": "Endpoint malware alert",
            "category": "Malware",
            "description": "An endpoint security tool detected a suspicious executable running from a temporary folder.",
            "answer": "Critical",
            "reason": "Execution from temporary folders can be associated with malware or suspicious scripts."
        },
        {
            "title": "Unusual PowerShell command",
            "category": "Malware",
            "description": "A workstation executed an encoded PowerShell command during non-business hours.",
            "answer": "Suspicious",
            "reason": "Encoded PowerShell commands can be used to hide malicious activity."
        },
        {
            "title": "Large download from cloud storage",
            "category": "Data Loss",
            "description": "A user downloaded 8 GB of files from cloud storage outside normal working hours.",
            "answer": "Suspicious",
            "reason": "Large downloads outside normal hours may indicate data exfiltration or unusual behavior."
        },
        {
            "title": "Sensitive file shared publicly",
            "category": "Data Loss",
            "description": "A document containing customer information was shared using a public link.",
            "answer": "Critical",
            "reason": "Public sharing of sensitive data creates a high risk of data exposure."
        },
        {
            "title": "User downloaded one PDF",
            "category": "Data Loss",
            "description": "A user downloaded one internal policy PDF during business hours.",
            "answer": "Benign",
            "reason": "This activity is normal and does not show clear signs of data loss."
        }
    ]


if __name__ == '__main__':
    main()