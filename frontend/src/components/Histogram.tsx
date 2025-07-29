// src/components/Histogram.tsx
import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from "recharts";

interface HistogramProps {
  data: any[];
  homeTeam: string;
  awayTeam: string;
}

const Histogram: React.FC<HistogramProps> = ({ data, homeTeam, awayTeam }) => {
  const bins = data.map((d) => d.bin);
  const min = Math.min(...bins);
  const max = Math.max(...bins);
  const BIN_SIZE = 10;

  const ticks = Array.from(
    { length: (max - min) / BIN_SIZE + 1 },
    (_, i) => min + i * BIN_SIZE
  );

  return (
    <div>
      <h2>Score Distribution</h2>
      <BarChart
        width={700}
        height={400}
        data={data}
        margin={{ top: 20, right: 30, left: 20, bottom: 20 }}
      >
        <XAxis
          dataKey="bin"
          label={{ value: "Runs", position: "bottom", offset: 0 }}
          tick={{ fontSize: 12 }}
          tickLine={false}
          ticks={ticks}
        />
        <YAxis
          label={{ value: "Frequency", angle: -90, position: "insideLeft" }}
          tick={{ fontSize: 12 }}
        />
        <Tooltip />
        <Legend verticalAlign="bottom" wrapperStyle={{ paddingTop: 40 }} />
        <Bar dataKey={homeTeam} fill="#53db3b" barSize={20} />
        <Bar dataKey={awayTeam} fill="#3b51db" barSize={20} />
      </BarChart>
    </div>
  );
};

export default Histogram;
