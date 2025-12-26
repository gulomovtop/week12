def analyze_campaigns(filename):
    with open(filename, "r") as file:
        total_interact = {}
        interact_list = []
        for line in file:
            line = line.strip().split(",")
            if len(line)<4:
                continue
            campaign_name = line[0]
            platform = line[1]
            clicks = line[2]
            shares = line[3]
            try:
                clicks = int(clicks)
                shares = int(shares)
                interactions = clicks+shares
            except ValueError as e:
                print(f"Handle lines aren't numbers {e}")
                continue
            if platform in total_interact:
                total_interact[platform] += interactions
            else:
                total_interact[platform] = interactions
            if interactions<1000:
                interact_list.append((campaign_name,interactions))
        return total_interact, interact_list
def save_marketing_report(platform_totals, bad_campaigns):
    with open("marketing_summary.txt", "w") as file2:
        file2.write(f"PLATFORM TRAFFIC VOLUME\n")
        file2.write(f"-----------------------\n")
        for platform, counts in platform_totals.items():
            file2.write(f"{platform}: {counts}\n")
        file2.write(f"\nCANCEL CAMPAIGNS (<1000 actions)\n")
        file2.write(f"-----------------------\n")
        for campaign_name, actions in bad_campaigns:
            file2.write(f"{campaign_name} ({actions} actions)\n")

platform_totals, bad_campaign = analyze_campaigns("campaign_data.txt")
save_marketing_report(platform_totals, bad_campaign)