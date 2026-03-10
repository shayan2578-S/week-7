## GitHub Copilot Chat

- Extension Version: 0.27.3 (prod)
- VS Code: vscode/1.100.2
- OS: Windows

## Network

User Settings:
```json
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 20.26.156.210 (20 ms)
- DNS ipv6 Lookup: Error (4 ms): getaddrinfo ENOTFOUND api.github.com
- Proxy URL: http://160.9.43.250:3128 (0 ms)
- Proxy Connection: 200 Connection established
	proxy-agent: Fortinet-Proxy/1.0 (13 ms)
- Electron fetch (configured): HTTP 200 (33 ms)
- Node.js https: HTTP 200 (34 ms)
- Node.js fetch: HTTP 200 (141 ms)
- Helix fetch: HTTP 200 (66 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.112.21 (14 ms)
- DNS ipv6 Lookup: Error (27 ms): getaddrinfo ENOTFOUND api.individual.githubcopilot.com
- Proxy URL: http://160.9.43.250:3128 (2 ms)
- Proxy Connection: 200 Connection established
	proxy-agent: Fortinet-Proxy/1.0 (84 ms)
- Electron fetch (configured): HTTP 200 (82 ms)
- Node.js https: HTTP 200 (258 ms)
- Node.js fetch: HTTP 200 (272 ms)
- Helix fetch: HTTP 200 (268 ms)

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).