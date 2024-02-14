#!/usr/bin/node

/**
 * This defines a Rectangle.
 */

module.exports = class Rectangle {
  /**
   * The constructor takes 2 arguments w and h.
   *
   * Creates an empty object if w or h is equal to 0 or not a positive integer
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Creates an instance method named print()
   * Prints the Rectangle of a character 'X'.
   */

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
