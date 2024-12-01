const TOTALS: number[] = [];

const readInput = async (path: string) => {
  const input = await Bun.file(path).text();
  const lines = input.trim().split("\n");
  const left = [];
  const right = [];
  for (const line of lines) {
    const [a, b] = line.split("  ");
    left.push(parseInt(a));
    right.push(parseInt(b));
  }
  return [left, right];
};

const grabAndRemoveSmallest = (arr: number[]) => {
  const smallest = Math.min(...arr);
  const index = arr.indexOf(smallest);
  arr.splice(index, 1);
  return { smallest, values: arr };
};

const calculateTotal = (left: number[], right: number[]) => {
  if (left.length === 0 || right.length === 0) {
    return;
  }
  const { smallest: l, values: lv } = grabAndRemoveSmallest(left);
  const { smallest: r, values: rv } = grabAndRemoveSmallest(right);
  TOTALS.push(Math.abs(l - r));
  calculateTotal(lv, rv);
};

const part1 = async () => {
  const [left, right] = await readInput("input.txt");
  calculateTotal(left, right);
  console.log(
    "Part One Solution",
    TOTALS.reduce((a, b) => a + b),
  );
};

const part2 = async () => {
  let total = 0;
  const [left, right] = await readInput("input.txt");
  for (const l of left) {
    total += l * right.filter((r) => r === l).length;
  }
  console.log("Part Two Solution", total);
};

const main = async () => {
  console.time("Part 1");
  await part1();
  console.timeEnd("Part 1");

  console.time("Part 2");
  await part2();
  console.timeEnd("Part 2");
};

main();

