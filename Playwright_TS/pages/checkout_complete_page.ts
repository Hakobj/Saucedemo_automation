import { Locator, Page } from '@playwright/test';
import { BasePage } from './base_page';

export class CheckoutCompletePage extends BasePage {
  readonly completeHeader: Locator;

  constructor(page: Page) {
    super(page);
    this.completeHeader = page.locator('.complete-header');
  }

  async verifyCompletion() {
    await this.expectText(this.completeHeader, 'Thank you for your order!');
  }
}