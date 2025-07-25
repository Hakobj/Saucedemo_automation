# Playwright End-to-End Automation – SauceDemo

This project uses [Playwright](https://playwright.dev/) with **TypeScript** and the **Page Object Model (POM)** design pattern to automate the end-to-end checkout flow of [SauceDemo.com](https://www.saucedemo.com).

---

## 📁 Project Structure

```
├── pages/                  # Page Object Model classes for each page
│   ├── base_page.ts
│   ├── login_page.ts
│   ├── inventory_page.ts
│   ├── cart_page.ts
│   ├── checkout_info_page.ts
│   ├── checkout_overview_page.ts
│   └── checkout_complete_page.ts
│
├── tests/                  # Test files
│   └── e2e_checkout_flow.spec.ts
│
├── test_data/             # Static test data
│   └── user_data.ts
│
├── .gitignore
├── package.json
├── package-lock.json
├── playwright.config.ts
└── tsconfig.json
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
npm install
```

### 2. Run the test

```bash
npx playwright test
```

### 3. View the test report (optional)

```bash
npx playwright show-report
```

---

## ✅ What the Test Covers

This test does the following:
- Logs in with a standard user
- Adds the first item to the cart
- Proceeds to checkout
- Enters user information
- Completes the order
- Verifies order completion

Each page includes **assertions** to ensure the correct screen is loaded.

---

## 🔧 Configuration

### Base URL
You can modify the site URL in `test_data/user_data.ts`:

```ts
export const testUser = {
  url: 'https://www.saucedemo.com/',
  ...
};
```

---

## 🛠 Useful Commands

| Command                         | Description                      |
|----------------------------------|----------------------------------|
| `npx playwright test`            | Run all tests                    |
| `npx playwright show-report`     | Open HTML report                 |
| `npx playwright codegen`         | Generate code via recorder       |
| `npx playwright install`         | Install browser binaries         |

---

## 📦 Dependencies

- `@playwright/test`
- `typescript`

---

## 🙅 .gitignore

Ensures that unwanted files like `node_modules/`, `test-results/`, etc., are not committed to Git.

---

## 📄 License

MIT License – feel free to use and adapt.