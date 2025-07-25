import { Locator, Page } from '@playwright/test';
import { BasePage } from './base_page';

export class InventoryPage extends BasePage {
  readonly addToCartButton: Locator;
  readonly cartIcon: Locator;

  constructor(page: Page) {
    super(page);
    this.addToCartButton = page.locator('button', { hasText: 'Add to cart' }).first();
    this.cartIcon = page.locator('.shopping_cart_link');
  }

  async addFirstItemToCart() {
    await this.click(this.addToCartButton);
  }

  async goToCart() {
    await this.click(this.cartIcon);
  }
}