module.exports = function (eleventyConfig) {
  // Pass the existing hand-built static site through to the build output untouched.
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("favicon.svg");
  eleventyConfig.addPassthroughCopy("robots.txt");
  eleventyConfig.addPassthroughCopy("sitemap.xml");
  eleventyConfig.addPassthroughCopy("llms.txt");
  eleventyConfig.addPassthroughCopy("vercel.json");
  eleventyConfig.addPassthroughCopy("*.html");
  eleventyConfig.addPassthroughCopy("backend-admin");

  // Readable date filter for post templates
  eleventyConfig.addFilter("readableDate", (d) => {
    const dt = (d instanceof Date) ? d : new Date(d);
    return dt.toLocaleDateString("en-US", {
      year: "numeric", month: "long", day: "numeric", timeZone: "UTC",
    });
  });
  eleventyConfig.addFilter("isoDate", (d) => {
    const dt = (d instanceof Date) ? d : new Date(d);
    return dt.toISOString().slice(0, 10);
  });

  return {
    dir: { input: ".", output: "_site", includes: "_includes", data: "_data" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
