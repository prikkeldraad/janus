# Janus
This application tracks versions of applications. The goal is to get a grip on life cycle of tools uses so you can be up to date. Nowadays many tools send update information when you use the tool, but sometime your tools are behind firewalls and you need to manually find out if you need to update. 
Janus gets info on new versions from the manufactures website and sends you a notification if there is an update.

Besides accurate information about the current available version, Janus will also scrape (or otherwise) obtain historical data on releases (via release notes for example) and predict the update cycle of the tool. So you can plan your maintenance upfront.

Janus is build in a container environment with microservices. Therefor there is no one language you need to use, as long as your service has an API it is ok.

GH HELP: https://cli.github.com/manual/gh_pr_checkout

# Install
1. Checkout repo
2. `make install`
3. `make run`
