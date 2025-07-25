
import { test } from '@playwright/test';
import { LoginPage } from '../pages/login_page';
import { InventoryPage } from '../pages/inventory_page';
import { CartPage } from '../pages/cart_page';
import { CheckoutInfoPage } from '../pages/checkout_info_page';
import { CheckoutOverviewPage } from '../pages/checkout_overview_page';
import { CheckoutCompletePage } from '../pages/checkout_complete_page';
import { testUser } from '../test_data/user_data';

test('End-to-End checkout flow', async ({ page }) => {
  await page.goto(testUser.url);

  const loginPage = new LoginPage(page);
  const inventoryPage = new InventoryPage(page);
  const cartPage = new CartPage(page);
  const checkoutInfoPage = new CheckoutInfoPage(page);
  const checkoutOverviewPage = new CheckoutOverviewPage(page);
  const checkoutCompletePage = new CheckoutCompletePage(page);

  await loginPage.login(testUser.username, testUser.password);
  await inventoryPage.addFirstItemToCart();
  await inventoryPage.goToCart();
  await cartPage.proceedToCheckout();
  await checkoutInfoPage.fillCheckoutInfo(testUser.firstName, testUser.lastName, testUser.postalCode);
  await checkoutOverviewPage.finishCheckout();
  await checkoutCompletePage.verifyCompletion();
});
