import { Locator, Page } from '@playwright/test';
import { BasePage } from './base_page';

export class CartPage extends BasePage {
  readonly checkoutButton: Locator;

  constructor(page: Page) {
    super(page);
    this.checkoutButton = page.locator('#checkout');
  }

  async proceedToCheckout() {
    await this.click(this.checkoutButton);
  }
}