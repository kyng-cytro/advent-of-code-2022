const readInput = async (path: string) => {
  const input = await Bun.file(path).text();
  const lines = input.trim().split("\n");
  return lines.map((line) => line.split(" ").map((num) => parseInt(num)));
};

const checkSafety = (row: number[]) => {
  const type = row[0] > row[1] ? "increasing" : "decreasing";
  for (let i = 0; i < row.length; i++) {
    if (i === 0) {
      continue;
    }
    const currType = row[i - 1] > row[i] ? "increasing" : "decreasing";
    if (currType !== type) {
      return false;
    }
    if (
      Math.abs(row[i] - row[i - 1]) > 3 ||
      Math.abs(row[i] - row[i - 1]) < 1
    ) {
      return false;
    }
  }
  return true;
};

const checkSafetyWithTolerance = (row: number[]) => {
  if (checkSafety(row)) {
    return true;
  }
  for (let i = 0; i < row.length; i++) {
    if (checkSafety([...row.slice(0, i), ...row.slice(i + 1)])) {
      return true;
    }
  }
  return false;
};

const part2 = async () => {
  let safes = 0;
  const data = await readInput("input.txt");
  for (const row of data) {
    if (checkSafetyWithTolerance(row)) {
      safes++;
    }
  }
  console.log("Part Two Solution", safes);
};

const part1 = async () => {
  let safes = 0;
  const data = await readInput("input.txt");
  for (const row of data) {
    if (checkSafety(row)) {
      safes++;
    }
  }
  console.log("Part One Solution", safes);
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
