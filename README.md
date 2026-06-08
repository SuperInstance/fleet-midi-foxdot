<div align="center">

# 🦊 fleet-midi-foxdot

> *Python live-coding MIDI engine for real-time fleet music*

[![CI](https://img.shields.io/github/actions/workflow/status/SuperInstance/fleet-midi-foxdot/ci.yml?style=flat-square&logo=github&label=CI)](https://github.com/SuperInstance/fleet-midi-foxdot/actions)
[![npm](https://img.shields.io/badge/npm-%40superinstance%2Fmidi--foxdot-cb3837?style=flat-square&logo=npm)](https://www.npmjs.com/package/@superinstance/midi-foxdot)
[![Docker](https://img.shields.io/badge/docker-ghcr-2496ed?style=flat-square&logo=docker)](https://github.com/SuperInstance/fleet-midi-foxdot/pkgs/container/fleet-midi-foxdot)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](http://makeapullrequest.com)

---

Bridges fleet agents to FoxDot for real-time Python live coding. Agent code becomes SuperCollider OSC messages — immediate audio from fleet decisions.

---

## 📦 Installation

```bash
# npm
npm install @superinstance/midi-foxdot

# Docker
docker pull ghcr.io/superinstance/fleet-midi-foxdot:latest

# Clone
git clone https://github.com/SuperInstance/fleet-midi-foxdot.git
```

## 🚀 Quick Start

```bash
# Send Python code to FoxDot:
curl -X POST localhost:3007 \
  -H "Content-Type: application/json" \
  -d "{\"code\":\"p1 >> pads([0,4,7], dur=4)\nClock.bpm = 100\"}"
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   Fleet Agent Code        FoxDot → SuperCollider     │
│   POST :3007              Clock.bpm = 120            │
│   {"code":"..."}          p1 >> pads([0,4,7])       │
│         │                 p2 >> bass([0,-2])        │
│         ▼                 p3 >> play("x-o-")         │
│   ┌──────────────┐                                   │
│   │ FoxDot       │───▶ OSC → SuperCollider → Audio  │
│   │ Bridge       │                                   │
│   └──────────────┘                                   │
│                                                     │
│   Python live-coding = music on the fly              │
│   Every fleet state becomes an OSC message           │
└─────────────────────────────────────────────────────┘
```

## 📡 API

### POST /
Send FoxDot Python code for live execution.

```json
{"code": "p1 >> pads([0,4,7], dur=4)"}
```
→ `{"status": "ok", "foxdot_code": "..."}`


## 🧪 Beta Tested

Part of the [SuperInstance MIDI Fleet](https://github.com/SuperInstance/construct-coordination/blob/main/FLEET_MIDI.md). Every push verified via CI — zeroshot tests ensure zero-config operation out of the box.

## 🤝 Related

- [fleet-bridge](https://github.com/SuperInstance/fleet-bridge) — I2I bottle transport
- [construct-coordination](https://github.com/SuperInstance/construct-coordination) — Fleet catalog

---

<div align="center">
<sub>Built with 🦊 for the SuperInstance fleet • <a href="https://github.com/SuperInstance">github.com/SuperInstance</a></sub>
</div>
