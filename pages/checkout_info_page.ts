import { Locator, Page } from '@playwright/test';
import { BasePage } from './base_page';

export class CheckoutInfoPage extends BasePage {
  readonly firstNameInput: Locator;
  readonly lastNameInput: Locator;
  readonly postalCodeInput: Locator;
  readonly continueButton: Locator;

  constructor(page: Page) {
    super(page);
    this.firstNameInput = page.locator('#first-name');
    this.lastNameInput = page.locator('#last-name');
    this.postalCodeInput = page.locator('#postal-code');
    this.continueButton = page.locator('#continue');
  }

  async fillCheckoutInfo(first: string, last: string, zip: string) {
    await this.type(this.firstNameInput, first);
    await this.type(this.lastNameInput, last);
    await this.type(this.postalCodeInput, zip);
    await this.click(this.continueButton);
  }
}