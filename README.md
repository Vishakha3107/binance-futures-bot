# Simplified Trading Bot (Binance Futures Testnet)

This is a multi-layered Python 3.x command-line utility application designed to place Market and Limit orders directly onto the Binance Futures Testnet (USDT-M) platform. 

The technical architecture and instructions outlined in this project directly satisfy the application task guidelines detailed in **DOC-20260602-WA0001..pdf**.

---

## Features
* **Multi-Layered Architecture:** Strict separation between the core Binance API client, trading execution logic, input validation, and the command-line interface (CLI).
* **Robust Local Validation:** Validates symbol formatting, trading sides, order types, positive quantities, and enforces price requirements for limit orders before network dispatch.
* **Robust Error Handling:** Catches and handles local input anomalies, invalid API credentials, exchange limitations, and network connection failures gracefully.
* **Structured Logging:** Seamless dual-logging system that routes operational tracing and API error exceptions cleanly into a local file (`logs/trading_bot.log`) while preserving a minimal, human-readable console interface[cite: 1].

---

## Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.x installed on your target machine[cite: 1]. 

### 2. Install Dependencies
Clone or download this repository, navigate to the root directory, and install the necessary requirements using `pip`[cite: 1]:
```bash
pip install -r requirements.txt
