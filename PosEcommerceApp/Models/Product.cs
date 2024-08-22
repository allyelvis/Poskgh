using System.ComponentModel.DataAnnotations;

public class Product
{
    public int Id { get; set; }
    [Required]
    public string Name { get; set; }
    [Required]
    [Range(0.01, double.MaxValue)]
    public decimal Price { get; set; }
    [Required]
    [Range(0, int.MaxValue)]
    public int Stock { get; set; }
}
