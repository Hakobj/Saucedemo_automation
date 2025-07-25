import { Locator, Page } from '@playwright/test';
import { BasePage } from './base_page';

export class CheckoutOverviewPage extends BasePage {
  readonly finishButton: Locator;

  constructor(page: Page) {
    super(page);
    this.finishButton = page.locator('#finish');
  }

  async finishCheckout() {
    await this.click(this.finishButton);
  }
}