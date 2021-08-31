# HTN-Goose-Counter
Hi! This is the public repository for our upcoming Hack the North workshop focused on Docker. Lets have fun!

## Deploying the app:
Step (1):
Create a GCP Project.

Step (2):
Enable Billing.

Step (3):
(a) Go to Compute Engine and create a new instance.
(b) Select Boot Disk as ****Container Optimized OS****
(c) Then click allow HTTP traffic under firewall

Step (4):
(a) Click on VPC Network, then go to Firewall
(b) Create a new rule:
    - Give it a name
    - Switch targets to all instances in network
    - Then in IP ranges add in ```0.0.0.0/0``` for all traffic
    - Under protocols and ports allow all

Step (5):
Connect to the VM by clicking on that SSH button

Step (6):
Clone the git repo: https://github.com/ehuan2/HTN-Goose-Counter.git (make sure this is the full solution branch)
```git clone https://github.com/ehuan2/HTN-Goose-Counter.git```

Step (7):
cd into HTN-Goose-Counter: ```cd HTN-Goose-Counter``` and then edit ```/src/frontend/public/main.html``` and replace the ```localhost``` with the external IPs.

Step (8):
Run the actual application by building each one according to the Makefile. Then run the following for docker-compose up:
```
docker run --rm \
    -w="$PWD" \
    docker/compose:1.24.0 up
```