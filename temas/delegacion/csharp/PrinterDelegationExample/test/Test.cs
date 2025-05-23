using NUnit.Framework;
using System;
using System.IO;

namespace PrinterDelegationExample.Tests
{
    public class PrinterManagerTests
    {
        [Test]
        public void ShouldDelegateToPdfPrinter()
        {
            // Arrange
            var manager = new PrinterManager();
            var printer = new PdfPrinter();
            var expectedOutput = "Printing PDF: Test Document";

            using (var sw = new StringWriter())
            {
                Console.SetOut(sw);

                // Act
                manager.SetPrinter(printer.Print);
                manager.PrintDocument("Test Document");

                // Assert
                var output = sw.ToString().Trim();
                Assert.AreEqual(expectedOutput, output);
            }
        }

        [Test]
        public void ShouldWarnWhenNoPrinterConfigured()
        {
            // Arrange
            var manager = new PrinterManager();
            var expectedOutput = "No printer configured.";

            using (var sw = new StringWriter())
            {
                Console.SetOut(sw);

                // Act
                manager.PrintDocument("Anything");

                // Assert
                var output = sw.ToString().Trim();
                Assert.AreEqual(expectedOutput, output);
            }
        }
    }
}
