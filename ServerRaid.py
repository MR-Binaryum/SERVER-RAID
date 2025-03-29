####Libs####

import subprocess
import requests
import re
import time
import dns.resolver
import ssl
import socket
from colorama import Fore, Style, init
from urllib.parse import urljoin

####Banner Function####

def Banner():

    print(f'''{Fore.LIGHTYELLOW_EX}   
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄               ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌             ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌          ▐░▌       ▐░▌  ▐░▌         ▐░▌  ▐░▌          ▐░▌       ▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀      ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌
          ▐░▌▐░▌          ▐░▌     ▐░▌        ▐░▌ ▐░▌      ▐░▌          ▐░▌     ▐░▌               ▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌        ▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌              ▐░▌      ▐░▌ ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌        ▐░▌        ▐░░░░░░░░░░░▌▐░▌       ▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀          ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀               ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  


                         
                                                            ___-----------___
                                                      __--~~                 ~~--__
                                                  _-~~                             ~~-_
                                                _-~                                     ~-_
                                              /                                           \
                                              |                                             |
                                            |                                               |
                                            |                                               |
                                            |                                                 |
                                            |                                                 |
                                            |                                                 |
                                            |                                               |
                                            |  |    _-------_               _-------_    |  |
                                            |  |  /~         ~\           /~         ~\  |  |
                                              ||  |     \|/     |         |      \| /   |  ||
                                              || |     -(O)-    |         |     -(O)-   | ||
                                              || |      /|\     |         |      /|\    | ||
                                              |   \_           /           \           _/   |
                                            |      ~~--_____-~    /~V~\    ~-_____--~~      |
                                            |                    |     |                    |
                                            |                    |       |                    |
                                            |                    |  /^\  |                    |
                                            |       _            ~~   ~~          _/         |
                                              \_       \ _                       _/         _/
                                                ~--____-~ ~\                   /~ ~-____--~
                                                    \     /\                 /\     /
                                                      \    | ( ,           , ) |    /
                                                      |   | (~(__(  |  )__)~) |   |
                                                        |   \/ (  (~~|~~)  ) \/   |
                                                        |   |  [ [  |  ] ]  /   |
                                                          |                     |
                                                          \                   /
                                                            ~-_             _-~
                                                              ~--___-___--~

''')
    

####Menu Options####

def Menuoption():
    subprocess.run("clear")
    Banner()
    print("")
    print(f'{Fore.MAGENTA}({Fore.LIGHTGREEN_EX}1{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Default Webpage download + data entry/file discover (Discovers: file paths and data entry from html tags)')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}2{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Server type discover (Discovers: the kind of server from a domain reading HEADERs from an HTTP GET request)')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}3{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Domain scraping (Discovers: robots.txt file, all href paths and DNS domains from SSL/TLS certificate)')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}4{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}DNS brute force attack (Discovers: all common subdomains, public IPs and DNS zone transfer from a domain)')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}5{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Download full webpage from a domain. (Downloads: all Front-end content of a website)')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}6{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Server supported HTTP methods (Discovers: all methods that an Server uses based on HTTP request/server code answer).')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}7{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Server Port scan/service discover (Discovers: Ports and his services from a domain)')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}8{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Requeriments install and conf (Libs and packets required to use the ServerRaid tool)')
    print(f'{Fore.LIGHTMAGENTA_EX}({Fore.LIGHTGREEN_EX}9{Fore.LIGHTMAGENTA_EX}){Fore.LIGHTCYAN_EX}--{Fore.LIGHTRED_EX}Exit (Exit of the program)')
    print("")
    print(f'{Fore.MAGENTA}╭─{Fore.LIGHTGREEN_EX}Select Attack mode (-_-){Fore.MAGENTA}')
    recognition = input("╰─$ ")
    
    handle_selection(recognition)

####Conditions if+elif+else of Menuoption####

def handle_selection(recognition):

    if recognition.isdigit():
        recognition = int(recognition)
    
        if (recognition) == 1:
            WDDEF()
        elif (recognition) == 2:
                SVP()    
        elif (recognition) == 3:
                SCRAPER()
        elif (recognition) == 4:
                DNSBRUTE()
        elif (recognition) == 5:
                fulldownload()
        elif (recognition) == 6:
                HTTPmethodDiscover()
        elif (recognition) == 7:
                Portscan()
        elif (recognition) == 8:
                Installconf()
        elif (recognition) == 9:
                Exit()
        else:
            print("wrong option dude :v")
            time.sleep(2)
    else:
        print("wrong option dude :v")
    time.sleep(2)
    Menuoption()

####Software Functions####

def WDDEF():
    def obtener_urls(base_url):
        try:
            # Mades an HTTP request with GET method.
            response = requests.get(base_url)
            response.raise_for_status()  # Launches an error if request fails

            # Find all urls of any kind of file using like reference href/src HTML tags
            hrefs = re.findall(r'href=["\'](.*?)["\']', response.text)
            srcs = re.findall(r'src=["\'](.*?)["\']', response.text)

            #lists to store diferent kind of URLs
            
            urls_html = set()
            urls_css = set()
            urls_js = set()
            urls_php = set()
            urls_image = set()
            urls_documents = set()

            # We process all href links
            for href in hrefs:
                full_urls = urljoin(base_url, href)
                if full_urls.endswith('.html'):
                    urls_html.add(full_urls)
                elif full_urls.endswith('.css'):
                    urls_css.add(full_urls)
                elif full_urls.endswith('.js'):
                    urls_js.add(full_urls)
                elif full_urls.endswith('.php'):
                    urls_php.add(full_urls)
                elif full_urls.endswith(('.jpg', '.png', '.jpeg', '.gif', '.csv')):
                    urls_image.add(full_urls)
                elif full_urls.endswith(('.doc', '.odt', '.txt', '.xls', '.pdf')):
                    urls_documents.add(full_urls)

            # We process all href src
            for src in srcs:
                full_urls = urljoin(base_url, src)
                if full_urls.endswith('.html'):
                    urls_html.add(full_urls)
                elif full_urls.endswith('.css'):
                    urls_css.add(full_urls)
                elif full_urls.endswith('.js'):
                    urls_js.add(full_urls)
                elif full_urls.endswith('.php'):
                    urls_php.add(full_urls)
                elif full_urls.endswith(('.jpg', '.png', '.jpeg', '.gif', '.csv')):
                    urls_image.add(full_urls)
                elif full_urls.endswith(('.doc', '.odt', '.txt', '.xls', '.pdf')):
                    urls_documents.add(full_urls)

            return {
                "HTML": urls_html,
                "CSS": urls_css,
                "JS": urls_js,
                "PHP": urls_php,
                "Images": urls_image,
                "Documents": urls_documents
            }

        except Exception as e:
            print(f"An error occurred: {e}")
            return {
                "HTML": set(),
                "CSS": set(),
                "JS": set(),
                "PHP": set(),
                "Images": set(),
                "Documents": set()
            }

    base_url = input("Enter url domain target: ")
    urls_extracted = obtener_urls(base_url)

    print(f'{Fore.LIGHTCYAN_EX}URLs HTML:')
    for url in urls_extracted["HTML"]:
        print(f'{Fore.LIGHTGREEN_EX}', url)

    print(f'{Fore.LIGHTCYAN_EX}URLs CSS:')
    for url in urls_extracted["CSS"]:
        print(f'{Fore.LIGHTGREEN_EX}', url)

    print(f'{Fore.LIGHTCYAN_EX}URLs JS:')
    for url in urls_extracted["JS"]:
        print(f'{Fore.LIGHTGREEN_EX}', url)

    print(f'{Fore.LIGHTCYAN_EX}URLs PHP:')
    for url in urls_extracted["PHP"]:
        print(f'{Fore.LIGHTGREEN_EX}', url)

    print(f'{Fore.LIGHTCYAN_EX}URLs Images:')
    for url in urls_extracted["Images"]:
        print(f'{Fore.LIGHTGREEN_EX}', url)

    print(f'{Fore.LIGHTCYAN_EX}URLs Documents:')
    for url in urls_extracted["Documents"]:
        print(f'{Fore.LIGHTGREEN_EX}', url)

####SVP function####
    ####Server type discover####

def SVP():
    url = input("Enter URL target: ")
    response = requests.get(url)

    print("HTTP Headers:")
    for header, value in response.headers.items():
         print(f'{header}: {value}')
         print("")  

####SCRAPER function####
    ####Domain scraping (Discover: robots.txt file, all href paths and DNS domains from SSL/TLS certificate)####

def SCRAPER():
    print("")

    url = input("Enter url: ")
    
    def get_certificate_info(url):
    # Extract hostname from url target
        host = url.split("//")[-1].split("/")[0]
    
    # Create an SSL context
        context = ssl.create_default_context()
    
    # Conect to server and get the certificate
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                return cert

    def print_certificate_dns(cert):
    # Print certificate info (Keys and values)
        print("Certificate information:")
        for key, value in cert.items():
            print(f"{key}: {value}")

    # get and show certificate information
    cert_info = get_certificate_info(url)
    print_certificate_dns(cert_info)

    print("")
    print("extracting full href paths from domain target:")
    command = f'curl -s -L "{url}" | grep -oP \'(?<=href=")[^"]*\' | awk \'{{if ($0 !~ /^https?:\\/\\//) print "https://{url}" $0; else print $0}}\''
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
         print(result.stdout)
    else:
         print(f"Error: {result.stderr}")

         # -----> 
# # 1) curl -s -L $page = download the page without showing the progress (-s) and redirect the results (-L)
# 2) | grep -oP (?<=href=")[^"]*' = use grep to support regular perl expression (-P) for extract all url find on href HTML tags ((?<=href=")[^"]*'), and only shows the part that match
# with the regular expression (-o)
# 3) | awk {if ($0 !~ /^https?:\/\//) print "$https://page" $0; else print $0}' = get the results from  last comamnd (|) and use awk for evaluate every URI extracted, 
# if the URI dont start by https ({if ($0 !~ /^https?:\/\//)), adds a prefix on the begin from line (print "$https://page" $0;

    try:
        robots = f'{url}/robots.txt'

        robotsreq = requests.get(robots)
        if robotsreq.status_code == 200:
            print(robotsreq.text)
        else: 
            print(f"Error to dump robots.txt file from: {robots}")

    except Exception as e:
            print(f'An error occurred: {e}')

####DNSBRUTE function####
    ####DNS brute force attack (Discover all common subdomains, public IPs and DNS zone transfer from a domain)####

def DNSBRUTE():

    subdomains = ["admin", "ads", "id", "images", "news", "alerts", "ns", "vdi", "ap", "dns", "upload", "ns1", "ns2", "apps", "ipv6", "ns3", "ldap", "download", "vpn", 
"web", "local", "mail", "blog", "chat", "www", "shop", "corp", "smtp", "mobile", "help", "home", "api", "dev", "test", "staging", "support", "downloads", "video", 
"docs", "dashboard", "secure", "git", "store", "status", "forum", "marketing", "careers", "events", "demo", "sandbox", "beta", "support2", "contact1", "contact2", 
"sales", "feedback", "resources", "media", "custom", "search", "support3", "info", "team", "partners", "knowledge", "pricing", "tickets", "tracking", "shop2", "training", 
"cloud", "community", "downloads2", "test2", "test3", "group", "tracking2", "push", "push2", "check", "link", "launch", "site", "checkout", "splash", "portal", "feedback2", 
"media2", "dev2", "analytics", "testapp", "devapp", "secure2", "api2", "api3", "webmail", "securemail", "billing", "office", "apps2", "mail2", "portal2", "store2", "shop3", 
"support4", "support5", "forum2", "devops", "data", "connect", "register", "dashboard2", "status2", "community2", "wiki2", "testbed", "search2", "user", "profile", "payment", 
"checkout2", "tasks", "calendars", "events2", "upload2", "assets", "static", "sandbox2", "devblog", "notifications", "updates", "files", "docs2", "team2", "partner2", "community3",
 "helpdesk", "careers2", "jobs", "about", "terms", "privacy", "corporate", "resources2", "knowledge2", "support6", "test3", "verify", "api4", "files2", "upload3", "links", "qr", 
 "auth", "auth2", "auth3", "verify", "authorize", "authenticate", "register2", "register3", "signin", "signout", "login2", "logout", "login3", "account", "profile2", "settings", 
 "manage", "manage2", "configure", "config", "options", "preference", "user2", "admin2", "moderator", "editor", "contributor", "publisher", "writer", "developer", "designer", 
 "analyst", "engineer", "manager", "director", "leader", "coordinator", "assistant", "advisor", "counselor", "mentor", "tutor", "instructor", "trainer", "coach", "therapist", 
 "consultant", "specialist", "expert", "master", "guru", "mentorship", "learning", "training2", "education", "academy", "institute", "school", "university", "collegiate", 
 "community2", "network2", "association", "society", "guild", "union", "league", "alliance", "team2", "partner3", "member", "subscriber", "benefactor", "donor", "sponsor", 
 "patron", "angel", "investor", "backer", "supporter", "volunteer", "contributor2", "participant", "attendee", "member2", "affiliate", "partner2", "associate", "colleague", 
 "colaborator", "collaborator", "fellow", "companion", "associate2", "affiliate2", "partner", "business", "venture", "enterprise", "corporation", "api-docs", "staging-api", 
 "legacy", "test-env", "live", "local-dev", "production", "testing", "int", "development", "qa", "sandbox-prod", "qa-env", "user-testing", "preprod", "workshop", "demo-env", 
 "demo-user", "staging-site", "feedback-loop", "welcome", "install", "issue-tracker", "bug-report", "error-log", "issue-log", "client-portal", "user-portal", "services", 
 "services2", "consulting", "consultation", "pre-sale", "post-sale", "user-guide", "help-center", "knowledge-base", "info-center", "faq", "support-articles", "docs-beta", 
 "service-status", "system-status", "api-status", "release-notes", "change-log", "roadmap", "privacy-policy", "terms-and-conditions", "compliance", "cookies-policy", 
 "disclaimer", "about-us", "team-bio", "history", "careers-page", "job-postings", "events-page", "announcements", "press", "media-kit", "resources-center", "downloads-page", 
 "community-forum", "social", "network", "hub", "partners-page", "affiliates", "profile-page", "user-profile", "contact-us", "get-in-touch", "contact-sales", "contact-support", 
 "find-us", "near-me", "locations", "store-locator", "newsletter", "subscriptions", "update-preferences", "alerts", "notifications2", "email-confirmation", "purchase-history", 
 "shopping-cart", "checkout-page", "wishlist", "favorites", "promotions", "offers", "deals", "coupons", "discounts", "specials", "gift-cards", "returns", "tracking-order", 
 "shipping-info", "user-uploads", "media-uploads", "form-submissions", "responses", "surveys", "polls", "feedback", "ideas", "suggestions", "user-feedback", "contact-form", 
 "community-feedback", "bug-tracker", "performance", "analytics2", "insights", "surveillance", "monitoring", "tests", "a/b-test", "bucket", "experiments", "conversion", 
 "optimization", "improvements", "agile", "sprints", "iteration", "roadmap", "timeline", "milestones", "deliverables", "sprint-reviews", "backlog", "user-stories", 
 "acceptance-criteria", "walkthrough", "prototypes", "layouts", "wireframes", "sketches", "blueprints", "tld", "history-archive", "old-site", "legacy-system", "deprecated", 
 "no-longer-supported", "current-versus-legacy", "archived", "previous-versions", "beta-features", "feature-requests", "issue-tracker", "support-tickets", "service-desk", 
 "incident-management", "change-management", "problem-management", "assets-management", "configuration-management", "dev-ops", "test-cases", "installation-guide", 
 "user-manual", "getting-started", "quick-start", "basic-config", "full-guide", "advanced-settings", "troubleshooting", "verified-setup", "setup-categories", "multi-language", 
 "localization", "translation", "feedback-loop", "work-in-progress", "change-requests", "feature-branch", "development-branch", "release-branch", "master-branch", "integration", 
 "delivery", "deployments", "staging-server", "production-server", "access", "permissions", "authentication", "user-roles", "tokens", "apks", "ios", "android", "mobile-app",
  "desktop-app", "extensions", "plugins", "premium", "add-ons", "third-party", "collaboration", "share", "export", "import", "synchronize", "sync", "connectivity", "update", 
  "backups", "backup2", "restore", "snapshot", "avatar", "pic", "image", "video", "podcast", "live-stream", "tattoos", "gallery", "showcase", "exhibit", "presentations", 
  "flowchart", "diagram", "charts", "imageset", "image-archive", "visuals", "design-assets", "guidelines", "style-guide", "branding", "identity", "theming", "color-schemes", 
  "project-portal", "collab-space", "collage", "collaboration-tools", "communication", "chats", "video-conferencing", "call", "webinars", "meetings", "discussion-boards", 
  "messaging", "emails", "inbox", "notifications", "alerts2", "updates", "reminders", "schedule", "calendars", "tasks2", "notes", "to-do", "lists", "shopping-lists", 
  "priorities", "inventory", "assets2", "supply", "consumption", "billing-info", "billing-history", "payments", "receipts", "transactions", "account-statements", "ledger", 
  "financials", "expenses", "costs", "revenue", "profit", "loss", "balance-sheet", "budget", "reports", "analysis", "projection", "forecast", "overviews", "calculators", 
  "dashboards", "monitoring2", "performance-metrics", "KPIs", "benchmarks", "goals", "outcomes", "results", "analysis-tools", "processor", "application", "api-docs2", "schema", 
  "data-model", "ERD", "data-dictionary", "data-warehouse", "data-lake", "dashboards2", "visualizations", "report-generator", "excel-export", "pdf-export", "csv-export", 
  "json-exports", "xml-exports", "analytics-dashboard", "trend-analyses", "projections", "statistics", "metrics", "summary", "highlight", "mobile", "desktop", "tablet", 
  "laptop", "sync-data", "share-data", "sync-time", "time-machine", "playbook", "how-to", "cases", "epics", "profiles", "console", "shell", "tools", "terminal", "env", 
  "scripts", "caches", "log", "debug", "trace", "proxies", "firewall", "vpn2", "secure-access", "metrics2", "sessions", "cloud-storage", "file-storage", "box", "drive", 
  "repository", "git-repo", "gitlab", "bitbucket", "github", "teamwork", "path", "redirection", "link-traffic", "affiliate-link", "metrics-tracking", "social-media", 
  "feather", "giant", "mesh", "networking", "webinar-host", "community-portal", "open-source", "project-repo", "collaboration-page", "feedback-loop", "ui-components", 
  "icons", "fonts", "sprites", "animations", "media-archive", "event-assets", "final-deliverables", "mockups", "prototyping", "user-testing", "beta-testing", "critical-path", 
  "delivery-keys", "documentation", "manuals", "external-docs", "standards", "conformance", "audits", "compliance-report", "regulatory", "policy-docs", "resources", "knowledge-hub", 
  "knowledge-check", "projects", "ideas-board", "brainstorming", "working-groups", "thought-leaders", "keynotes", "workshops", "summits", "webinars2", "course", "curriculum", 
  "lesson", "module", "program", "sessions2", "enrollment", "open-registrations", "rsvp", "apply", "scholarship", "grants", "funding", "resources3", "grant-management", 
  "member-area", "exclusive", "premium-content", "patreon", "support-program", "donation", "contribute", "fundraise", "pledge", "capital", "donations", "give", "gift", 
  "sponsorship", "partner-program", "collab-partners", "expanded-growth", "networking-events", "cultivate", "impact", "outreach", "effect", "influence", "buzz", 
  "word-of-mouth", "advocate", "support-a-cause", "help-others", "return-on-investment", "results-driven", "outcomes-based", "effectivity", "efficiency", "operational", 
  "value", "social-impact", "positive-change", "transformation", "innovation", "breakthrough", "leadership", "mentoring", "coaching", "lifelong-learning", "improvement", 
  "reflect", "debrief", "share-learning", "inspiration", "ignite", "inspire", "motivate", "vision", "strategy", "strategic-planning", "process", "efficacy", "effectiveness", 
  "integration", "join", "unite", "together", "collaborate", "convene", "host", "facilitate", "connector", "synergy", "connect", "unify", "confluence", "merge"]

    DNSzoneTransfer = ["A","NS","MX","HINFO","TXT","PTR","AAAA","SOA"]

    domain = input(f"{Fore.LIGHTCYAN_EX}Enter the domain: ")

    # open file in read mode
    with open("subdomains.txt", "w") as file:
        for record_type in DNSzoneTransfer:
            for subdomain in subdomains: 
                full_domain = f"{subdomain}.{domain}"
                try:
                    answers = dns.resolver.resolve(full_domain, record_type)  
                    for rdata in answers:
                        result = f"{full_domain} - {record_type}: {rdata}\n"
                        print(f'{Fore.LIGHTYELLOW_EX}', result.strip())
                        file.write(result)  
                except dns.resolver.NoAnswer:
                    result = f"{full_domain} - {record_type}: No answer\n"
                    print(f'{Fore.LIGHTYELLOW_EX}', result.strip())
                    file.write(result)
                except dns.resolver.NXDOMAIN:
                    result = f"{full_domain} - {record_type}: Does not exist\n"
                    print(f'{Fore.LIGHTYELLOW_EX}', result.strip())
                    file.write(result)
                except Exception as e:
                    result = f"{full_domain} - {record_type}: Error: {e}\n"
                    print(f'{Fore.LIGHTYELLOW_EX}', result.strip())
                    file.write(result)


####fulldownload function####
    ####Download full webpage content from a domain.####

def fulldownload():
    print(f'{Fore.MAGENTA}╭─{Fore.LIGHTGREEN_EX}Enter webpage domain (www.domain.example) (-_-){Fore.MAGENTA}')
    page = input("╰─$ ")
    subprocess.run('wget --mirror --convert-links --adjust-extension --page-requisites --no-parent --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" ', (page))

####HTTPmethodDiscover function####
    ####Server supported HTTP methods (Discover all methods that an Server uses based on HTTP request/server code answer).####

def HTTPmethodDiscover():
    init(autoreset=True)
    target = input(f"{Fore.LIGHTCYAN_EX}Enter the protocol:domain to test HTTP methods request: ")
    methods = [
    "GET",        # Retrieve data
    "POST",       # Send data to create a new resource
    "PUT",        # Update an existing resource
    "HEAD",       # Retrieve the headers of a resource
    "PATCH",      # Partially modify a resource
    "TRACE",      # Perform a message loop-back test along the path to the resource
    "CONNECT",    # Establish a tunnel to the server identified by the target resource
    "OPTIONS",    # Describe the communication options for the target resource
    "DELETE",     # Remove a resource
    "COPY",       # Copy a resource from one location to another (non-standard)
    "LINK",       # Establish a relationship between two resources (non-standard)
    "UNLINK",     # Remove a relationship between two resources (non-standard)
    "PURGE",      # Remove a resource from cache (used in some proxies)
    "LOCK",       # Lock a resource to prevent modifications (WebDAV)
    "UNLOCK",     # Unlock a resource (WebDAV)
    "PROPFIND",   # Retrieve properties of a resource (WebDAV)
    "PROPPATCH",  # Modify properties of a resource (WebDAV)
    "MKCOL",      # Create a collection of resources (WebDAV)
    "MOVE",       # Move a resource from one location to another (WebDAV)
    "SEARCH",     # Search for resources (used in some APIs)
    "SUBSCRIBE",  # Subscribe to a resource for updates (used in WebSub)
    "UNSUBSCRIBE",# Unsubscribe from a resource (used in WebSub)
    "NOTIFY",     # Send notifications about resource changes (used in WebSub)
    "REPLACE",    # Replace a resource entirely (non-standard)
    "MERGE",      # Merge changes into a resource (non-standard)
    "REPORT",     # Generate a report on a resource (WebDAV)
    "CHECKOUT",   # Check out a resource for editing (WebDAV)
    "CHECKIN",    # Check in a resource after editing (WebDAV)
    "VERSION-CONTROL", # Manage versions of a resource (WebDAV)
    "BASELINE-CONTROL", # Control baselines of a resource (WebDAV)
    "ACL",        # Manage access control lists (WebDAV)
    "BIND",       # Bind a resource to a URI (WebDAV)
    "REBIND",     # Rebind a resource to a new URI (WebDAV)
    "UNBIND",     # Unbind a resource from a URI (WebDAV)
    "CREATE",     # Create a new resource (non-standard)
    "GET-ACL",    # Retrieve the access control list for a resource (WebDAV)
    "SET-ACL",    # Set the access control list for a resource (WebDAV)
    "GET-LOCK",   # Retrieve the lock information for a resource (WebDAV)
    "SET-LOCK",   # Set a lock on a resource (WebDAV)
    "GET-RESOURCE", # Retrieve a resource (non-standard)
    "SET-RESOURCE", # Set a resource (non-standard)
]

# Response codes

    status_colors = {
    200: Fore.GREEN,   # OK
    201: Fore.GREEN,   # Created
    204: Fore.GREEN,   # No Content
    301: Fore.YELLOW,  # Moved Permanently
    302: Fore.YELLOW,  # Found (Redirect)
    303: Fore.YELLOW,  # See Other
    304: Fore.YELLOW,  # Not Modified
    400: Fore.RED,     # Bad Request
    401: Fore.RED,     # Unauthorized
    403: Fore.RED,     # Forbidden
    404: Fore.RED,     # Not Found
    405: Fore.RED,     # Method Not Allowed
    409: Fore.RED,     # Conflict
    415: Fore.RED,     # Unsupported Media Type
    500: Fore.WHITE,     # Internal Server Error
    501: Fore.WHITE,     # Not Implemented
    503: Fore.WHITE,     # Service Unavailable
}

    def try_method(method):
        try:
            print(f'{Fore.CYAN} Trying method: {Fore.LIGHTMAGENTA_EX}{method}')
            response = requests.request(method, target)
            color = status_colors.get(response.status_code, Fore.WHITE)
            print(f'Method: {method} - Response Code: {color}{response.status_code}{Style.RESET_ALL}')

        except Exception as e:
            print(f'Method: {method} - Error: {Fore.RED}{str(e)}{Style.RESET_ALL}')

    for method in methods:
        try_method(method)

####Portscan function####
    ####Server Port scan/service discover#####

def Portscan():
    target = input(f"{Fore.LIGHTCYAN_EX}Enter IP address from target: ")
    time.sleep(2)
    with open("output.txt", "a") as output_file: 
         subprocess.run(["sudo", "proxychains", "nmap", "-sV", "-O","-T4", target],stdout=output_file)

####Installconf function####
    ####Requeriments install and conf#####

def Installconf():
    subprocess.run(["sudo", "apt", "install", "wget", "python3", "git", "nmap", "python3-requests", "python3-colorama","python3-dnspython",  "proxychains", "torsocks", "tor", "-y"]),
    subprocess.run(["sudo", "cp", "/etc/proxychains.conf", "/etc/proxychains.conf.bck"]),
    subprocess.run(['"echo"', '""', ">", "/etc/proxychains.conf"]),
    subprocess.run(["echo", "socks5",  "127.0.0.1", "9050", ">", "/etc/proxychains.conf", "&&", "cd", "$HOME"]),
    subprocess.run(["echo", "source", "torsocks", "on", ">>", "/home/$USER/.bashrc"]),
    subprocess.run(["source", "torsocks", "on"])

####Exit function####
    ####Exit of program#####

def Exit():
    print(f"{Fore.LIGHTRED_EX} BYEEE >:)")
    quit()

    ####Calls Menuoptions function####
Menuoption()